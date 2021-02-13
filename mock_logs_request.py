import requests
import argparse
import json
import random

from functools import partial
from concurrent.futures import ThreadPoolExecutor


def generate_random_ip(number):

    payload = []
    for _ in range(number):
        ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        data = {
            "timestamp": "2020-06-24T15:27:00.123456Z",
            "ip": ip,
            "url": "placeholder_url",
        }

        data = json.dumps(data)
        payload.append(data)

    return payload


def send_request(data, host, port):
    URL = f"http://{host}:{port}/logs"
    result = requests.post(url=URL, data=data)
    print(result.response)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test Requests")
    parser.add_argument("--number", type=int, default=1)
    parser.add_argument("--port", default=5000)
    parser.add_argument("--host", default="0.0.0.0")
    args = parser.parse_args()

    payload = generate_random_ip(args.number)
    request = partial(send_request, host=args.host, port=args.port)
    with ThreadPoolExecutor(max_workers=12) as executor:
        executor.map(request, payload)
