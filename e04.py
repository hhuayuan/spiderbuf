# coding=utf-8

import requests
from lxml import etree
import re

base_url = 'https://spiderbuf.cn/web-scraping-practice/block-ip-proxy'

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

proxies = {'http':'47.122.65.254:8080'}
# 取页数
html = requests.get(base_url, headers=myheaders,proxies=proxies).text
root = etree.HTML(html)
# print(html)
lis = root.xpath('//ul[@class="pagination"]/li/a')
pages = []
for item in lis:
    print(item.attrib['href'])
    if item.attrib['class'] != 'item trap':
        pages.append(item.attrib['href'])
print(pages)
i = 1
for item in pages:
    print(item)
    s = item.replace('/web-scraping-practice/block-ip-proxy','')
    print(base_url + s)
    url = base_url + s
    # print(url)
    html = requests.get(url, headers=myheaders).text
    # print(html)
    #
    f = open('./data/e04/e04_%d.html' % i, 'w', encoding='utf-8')
    f.write(html)
    f.close()
    #
    root = etree.HTML(html)
    trs = root.xpath('//tr')

    f = open('./data/e04/e04_%d.txt' % i, 'w', encoding='utf-8')
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
    i += 1
