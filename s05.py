# coding=utf-8

import requests
from lxml import etree

url = 'https://spiderbuf.cn/web-scraping-practice/scraping-images-from-web'

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}


html = requests.get(url, headers=myheaders).text
print(html)

f = open('05.html', 'w', encoding='utf-8')
f.write(html)
f.close()

root = etree.HTML(html)
imgs = root.xpath('//img/@src')
print(imgs)
for item in imgs:
    img_data = requests.get('https://spiderbuf.cn' + item, headers=myheaders).content
    img = open(str(item).replace('/',''), 'wb')
    img.write(img_data)
    img.close()
#
# f = open('data05.txt', 'w', encoding='utf-8')
# for tr in trs:
#     tds = tr.xpath('./td')
#     s = ''
#     for td in tds:
#         s = s + str(td.xpath('string(.)')) + '|'
#         # s = s + str(td.text) + '|'
#     print(s)
#     if s != '':
#         f.write(s + '\n')
#
# f.close()
