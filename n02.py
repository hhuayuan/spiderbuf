# coding=utf-8

import requests
from lxml import etree

import base64

url = 'https://spiderbuf.cn/web-scraping-practice/scraping-images-base64'

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}


html = requests.get(url, headers=myheaders).text
print(html)

f = open('./data/n02/n02.html', 'w', encoding='utf-8')
f.write(html)
f.close()

root = etree.HTML(html)
imgs = root.xpath('//img/@src')
print(imgs)
for item in imgs:
    print(item)
    # item 是获取到的base64字符串
    item = item.replace('data:image/png;base64,','')
    str_bytes = item.encode('raw_unicode_escape')  # str 转 bytes
    decoded = base64.b64decode(str_bytes)

    img = open('./data/n02/n02.png', 'wb')
    img.write(decoded)
    img.close()

