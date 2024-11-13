# coding=utf-8

import requests
from lxml import etree

base_url = 'https://spiderbuf.cn/playground/n07'

my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

# 取页数
html_bytes = requests.get(base_url, headers=my_headers).content
html = html_bytes.decode()
root = etree.HTML(html)
with open('./data/n07/n07.html', 'w', encoding='utf-8') as f:
    f.write(html)
# print(html)
divs = root.xpath('/html/body/main/div[2]/div')
with open('./data/n07/n07.txt','w',encoding='utf-8') as f:
    for div in divs:
        print(div.text)
        if div.text:
            f.write(f'{div.text}\n')