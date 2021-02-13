import requests
import argparse
import json
import random

from functools import partial
from concurrent.futures import ThreadPoolExecutor


def send_request(host, port):
    URL = f"http://{host}:{port}/metrics"
    result = requests.get(url=URL)
    print(f"Number of unique IPs present since last start-up time is {int(result.content)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test Requests")
    parser.add_argument("--port", default=9102)
    parser.add_argument("--host", default="0.0.0.0")
    args = parser.parse_args()

    send_request(host=args.host, port=args.port)
