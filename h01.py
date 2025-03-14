# coding=utf-8

import requests
from lxml import etree

url = 'https://spiderbuf.cn/web-scraping-practice/scraping-css-confuse-offset'

myheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
             'Referer':'https://spiderbuf.cn/list'}

html = requests.get(url, headers=myheaders).text
print(html)

f = open('./data/h01/h01.html', 'w', encoding='utf-8')
f.write(html)
f.close()

root = etree.HTML(html)
ls = root.xpath('//div[@class ="container"]/div/div')
# page_text = ls[0].xpath('string(.)')
# print(page_text)

f = open('./data/h01/h01.txt', 'w', encoding='utf-8')
for item in ls:
    hnodes = item.xpath('./h2')
    temp = hnodes[0].xpath('string(.)')
    s0 = temp[1:2] + temp[0:1] + temp[2:]
    print(s0)

    pnodes = item.xpath('./p')
    s1 = pnodes[0].text
    print(s1)
    temp = pnodes[1].xpath('string(.)').replace('企业估值(亿元)：','')
    s2 = temp[1:2] + temp[0:1] + temp[2:]
    print(s2)
    s3 = pnodes[2].text
    print(s3)
    s4 = pnodes[3].text
    print(s4)
    # 富邦金融控股排名：50企业估值(亿元)：2135CEO：蔡明兴行业：金融服务
    s = s0 + '|' + s1.replace('排名：','') + '|' + s2.replace('企业估值(亿元)：','') + '|' \
        + s3.replace('CEO：','') + '|' + s4.replace('行业：','') + '\n'
    print(s)
    f.write(s)

f.close()