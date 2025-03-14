# coding=utf-8

import requests
from lxml import etree

url = 'https://spiderbuf.cn/web-scraping-practice/scraper-login-username-password/login'

myheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

payload = {'username':'admin','password':'123456'}

html = requests.post(url, headers=myheaders, data=payload).text
print(html)

f = open('./data/e01/e01.html', 'w', encoding='utf-8')
f.write(html)
f.close()

root = etree.HTML(html)
trs = root.xpath('//tr')

f = open('./data/e01/data_e01.txt', 'w', encoding='utf-8')
for tr in trs:
    tds = tr.xpath('./td')
    s = ''
    for td in tds:
        # print(td.text)
        s = s + str(td.text) + '|'
    print(s)
    if s != '':
        f.write(s + '\n')

f.close()

