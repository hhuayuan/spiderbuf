# coding=utf-8
import base64
import hashlib
import time

import requests
from lxml import etree
from selenium import webdriver


base_url = 'https://spiderbuf.cn/web-scraping-practice/javascript-reverse-timestamp'

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

def getHTML(url,file_name=''):
    client = webdriver.Chrome()
    client.get(url)
    time.sleep(5)
    html = client.page_source
    print(html)
    client.quit()

    if file_name != '':
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(html)
    return html


def parseHTML(html,file_name=''):
    root = etree.HTML(html)
    trs = root.xpath('//tr')

    if file_name != '':
        f = open(file_name, 'w', encoding='utf-8')

    for tr in trs:
        tds = tr.xpath('./td')
        s = ''
        for td in tds:
            s = s + str(td.xpath('string(.)')) + '|'
            # s = s + str(td.text) + '|'
        print(s)
        if (s != '') & (file_name != ''):
            f.write(s + '\n')
    f.close()


if __name__ == '__main__':
    # example: 1
    html = getHTML(base_url, './data/h05/h05.html')
    # parseHTML(html, './data/h04/h04.txt')

    # example: 2
    # url = 'https://spiderbuf.cn/web-scraping-practice/javascript-reverse-timestamp/api/'
    # timestamp = str(int(time.time()))
    # md5_hash = hashlib.md5()
    # md5_hash.update(timestamp.encode('utf-8'))
    # md5 = md5_hash.hexdigest()
    # s = ('%s,%s' % (timestamp, md5))
    # print(s)
    # payload = str(base64.b64encode(s.encode('utf-8')), 'utf-8')
    # print(payload)
    # html = requests.get(url + payload, headers=myheaders).text
    # print(html)
