# coding=utf-8

import requests
from lxml import etree
import time

base_url = 'http://www.spiderbuf.cn/n03/%d'

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

max_no = 20
# exit()

for i in range(1, max_no + 1):
    print(i)
    url = base_url % i
    print(url)
    html = requests.get(url, headers=myheaders).text
    print(html)

    f = open('./data/n03/n03_%d.html' % i, 'w', encoding='utf-8')
    f.write(html)
    f.close()

    root = etree.HTML(html)
    trs = root.xpath('//tr')

    f = open('./data/n03/datan03_%d.txt' % i, 'w', encoding='utf-8')
    for tr in trs:
        tds = tr.xpath('./td')
        s = ''
        for td in tds:
            s = s + str(td.xpath('string(.)')) + '|'
            # s = s + str(td.text) + '|'
        print(s)
        if s != '':
            f.write(s + '\n')
    time.sleep(2)
    f.close()
