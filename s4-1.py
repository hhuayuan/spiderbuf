# coding=utf-8

import requests
from lxml import etree
import re

url = 'http://www.spiderbuf.cn/playground/s04?pageno=2&pagesize=50'

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

html = requests.get(url, headers=myheaders).text
print(html)

f = open('./data/4-1/04-1.html', 'w', encoding='utf-8')
f.write(html)
f.close()

root = etree.HTML(html)
trs = root.xpath('//tr')

f = open('./data/4-1/data04-1.txt', 'w', encoding='utf-8')
for tr in trs:
    tds = tr.xpath('./td')
    s = ''
    for td in tds:
        s = s + str(td.xpath('string(.)')) + '|'
        # s = s + str(td.text) + '|'
    print(s)
    if s != '':
        f.write(s + '\n')

f.close()
