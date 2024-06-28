# -*- coding: utf-8 -*-
import requests
import json
import argparse


# 设置argparse
parser = argparse.ArgumentParser(description='Send a POST request to a RESTful API and extract the answer field from the JSON response.')
parser.add_argument('--query', type=str, required=True, help='The query parameter to be sent in the request data.')

# 解析命令行参数
args = parser.parse_args()

# RESTful API的URL
url = 'http://10.3.71.126/v1/chat-messages'

# 要发送的数据
data = {
    "inputs": {},
    "query": args.query,
    "response_mode": "blocking",
    "user": "lijinlong9"
}

# 设置HTTP头参数
headers = {
    'Authorization': 'Bearer app-5fR5J8ljjjBtXKYIv1qM8JW1',
    'Content-Type': 'application/json'
}

# 发送POST请求
response = requests.post(url, headers=headers, data=json.dumps(data))

# 检查请求是否成功
if response.status_code == 200:
    # 解析返回的JSON数据
    response_json = response.json()

    # 提取answer字段的内容
    answer = response_json.get('answer')

    # 打印answer字段的内容
    if answer is not None:
        print(answer)
    else:
        print("The 'answer' field was not found in the response.")
else:
    print(f"Failed to get a successful response, status code: {response.status_code}")