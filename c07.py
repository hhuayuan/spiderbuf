# coding=utf-8

import requests
from lxml import etree
import time
import json
import hashlib
import random
import numpy as np

base_url = 'https://spiderbuf.cn/web-scraping-practice/scraper-practice-c07'

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

if __name__ == '__main__':
    html = requests.get(base_url).text
    root = etree.HTML(html)
    inputs = root.xpath('//input[@id="token"]/@value')
    token = ''
    if len(inputs) > 0:
        token = inputs[0]
    print(token)
    key = "ZJC5WYHw7NNAWr8Vj8V1wjBpktGlT70j"
    random_value = random.randint(2000, 10000)
    timestamp = int(time.time())
    md5_hash = hashlib.md5()
    md5_hash.update(f'{token}{timestamp}{key}'.encode('utf-8'))
    hash = md5_hash.hexdigest()
    payload = {
        'key': key,
        'timestamp': timestamp,
        'token': token,
    }
    myheaders['cookie'] = f'_asd2sdf99={hash}'
    json_response = requests.post(base_url, headers=myheaders,json=payload).text

    cpc_arr = []
    json_data = json.loads(json_response)
    for item in json_data:
        c = int(item['cpc_usd'])
        m = int(item['monthly_search_volume'])
        cpc_arr.append((c^m)/100)

    print(np.average(cpc_arr))
