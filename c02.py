# coding=utf-8

import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.common.by import By
import time
import base64
import json
import numpy as np


base_url = 'https://spiderbuf.cn/web-scraping-practice/scraper-practice-c02'

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

def getHTML(url,file_name=''):
    client = webdriver.Chrome()
    client.get(url)
    time.sleep(10)

    # 事件参数对象
    actionChains = ActionChains(client)

    # 捕捉滑块元素
    slide_btn = client.find_element(By.ID, 'slider')
    # 观察网站滑块移动的长度和位置
    actionChains.click_and_hold(slide_btn)
    actionChains.move_by_offset(220,0)
    # 这里要注意：
    # 以下三个是以上面的坐标(220,0)为起点来计算的
    # 所以最终移动的距离是220加上以下的累计
    actionChains.move_by_offset(11,0)
    actionChains.move_by_offset(13,0)
    actionChains.move_by_offset(10,0)

    actionChains.release()
    actionChains.perform()

    html = client.page_source
    print(html)
    client.quit()

    if file_name != '':
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(html)
    return html


def parseHTML(html):
    root = etree.HTML(html)
    trs = root.xpath('//tr')

    prices = []
    for tr in trs:
        tds = tr.xpath('./td')
        if len(tds) > 2:
            prices.append(int(tds[2].text))
    print(prices)
    print(np.mean(prices))


if __name__ == '__main__':
    # example: 1
    html = getHTML(base_url, './data/c02/c02.html')
    parseHTML(html)

    # example: 2
    # html = requests.get(base_url, headers=myheaders).text
    # a = html.index('encryptedData = "') + 17
    # html = html[a:]
    # b = html.index('";')
    # html = html[:b]
    # print(html)
    # dic = eval(base64.b64decode(html.encode('utf-8')))
    # objs = dic['flights']
    # prices = []
    # for obj in objs:
    #     print(obj)
    #     prices.append(obj['price'])

    # print(prices)
    # print(np.mean(prices))

