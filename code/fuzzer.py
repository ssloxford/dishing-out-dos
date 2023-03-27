#!/usr/bin/python3

# Iterate through all commands of length 3 with a trailing zero byte
# Log those that do not return error code 13 (invalid) or 12 (unimplemented)

import requests, random
from tqdm import tqdm

url = "http://192.168.100.1:9201/SpaceX.API.Device.Device/Handle"
headers = {
    "Accept": "*/*",
    "Accept-Language": "en-GB,en;q=0.5",
    "content-type": "application/grpc-web+proto",
    "x-grpc-web": "1"
}
def send_request(data):
    response = requests.post(url, data=data, headers=headers)
    return dict(
        data=data,
        status_code=response.status_code,
        headers=response.headers,
        content=response.content
    )
def generate_bytes(length, length_header=None, continue_from=None):
    length_header = length_header or length
    continue_from = continue_from or 0
    preamble = b'\x00\x00\x00\x00' + length_header.to_bytes(1, 'big')
    for i in range(continue_from, 256**length):
        yield preamble + i.to_bytes(length, 'big')
results = []
for data in tqdm(generate_bytes(2, length_header=3), total=256**2):
    data = data + b'\x00'
    response = send_request(data)
    if response['headers'].get('grpc-status') != '13' and response['headers'].get('grpc-status') != '12':
        print("Found something!")
        print(response)
        results.append((data, response))
