# coding=utf-8

import requests
from lxml import etree
import re

base_url = 'https://spiderbuf.cn/web-scraping-practice/web-pagination-scraper?pageno=%d'

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

# 取页数
html = requests.get(base_url % 1, headers=myheaders).text
root = etree.HTML(html)

lis = root.xpath('//ul[@class="pagination"]/li')
page_text = lis[0].xpath('string(.)')
ls = re.findall('[0-9]', page_text)

max_no = int(ls[0])
# exit()

for i in range(1, max_no + 1):
    print(i)
    url = base_url % i
    print(url)
    html = requests.get(url, headers=myheaders).text
    print(html)

    f = open('04_%d.html' % i, 'w', encoding='utf-8')
    f.write(html)
    f.close()

    root = etree.HTML(html)
    trs = root.xpath('//tr')

    f = open('data04_%d.txt' % i, 'w', encoding='utf-8')
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
