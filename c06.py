# coding=utf-8

import requests
import time
from lxml import etree
import hashlib
import json

base_url = 'https://spiderbuf.cn/web-scraping-practice/scraper-practice-c06'

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'Cookie':'_asd2sdf99=gvGAJJbfZxDhI17Eu59KPhAkT1nzJ6zM;'}

if __name__ == '__main__':
    # 先取页面中的固定数据
    total = 0
    html = requests.get(base_url,headers=myheaders).text

    root = etree.HTML(html)
    spans = root.xpath('//div[@class="detail"]/p[1]/span[2]')
    for span in spans:
        total += float(span.text)
    print(f"{total:.2f} ")

    random_value = 3006
    timestamp = int(time.time())
    md5_hash = hashlib.md5()
    md5_hash.update(f'{random_value}spiderbuf{timestamp}'.encode('utf-8'))
    hash = md5_hash.hexdigest()
    payload = {
        'random': random_value,
        'signture': hash,
        'timestamp': timestamp,        
    }
    # print(payload)
    result = requests.post(base_url, headers=myheaders,json=payload).text

    json_data = json.loads(result)

    for item in json_data:
        print(item['rating'])
        total += float(item['rating'])

    print(f'{total:.2f}')
