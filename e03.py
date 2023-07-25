# coding=utf-8

import requests
from lxml import etree
import re

base_url = 'http://spiderbuf.cn/e03'
# http://spiderbuf.cn/e03/5f685274073b

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

# 取页数
html = requests.get(base_url, headers=myheaders).text
root = etree.HTML(html)
print(html)
# <li><span>共5页</span></li>
# <li><a href="./2fe6286a4e5f">1</a></li>
# <li><a href="./5f685274073b">2</a></li>
# <li><a href="./279fcd874c72">3</a></li>
# <li><a href="./8a3d4d640516">4</a></li>
# <li><a href="./fbd076c39d28">5</a></li>
lis = root.xpath('//ul[@class="pagination"]/li/a/@href')
print(lis)
# ['./2fe6286a4e5f', './5f685274073b', './279fcd874c72', './8a3d4d640516', './fbd076c39d28']
i = 1
for item in lis:
    print(item)
    s = item.replace('.','')
    print(base_url + s)
    url = base_url + s
    # print(url)
    html = requests.get(url, headers=myheaders).text
    # print(html)
    #
    f = open('./data/e03/e03_%d.html' % i, 'w', encoding='utf-8')
    f.write(html)
    f.close()
    #
    root = etree.HTML(html)
    trs = root.xpath('//tr')

    f = open('./data/e03/e03_%d.txt' % i, 'w', encoding='utf-8')
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