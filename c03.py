# coding=utf-8

import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import hashlib
import random
import numpy as np


base_url = 'https://spiderbuf.cn/web-scraping-practice/scraper-practice-c03'

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

def getHTML(url,file_name=''):
    sepal_width_arr = []
    client = webdriver.Chrome()
    client.get(url)
    time.sleep(5)
    html = client.page_source
    # print(html)
    parseHTML(html,sepal_width_arr)
    if file_name != '':
        with open(file_name + '_1.html', 'w', encoding='utf-8') as f:
            f.write(html)
    for i in range(1,5):
        client.find_elements(By.XPATH, '//ul/li/a')[i].click()
        time.sleep(5)
        html = client.page_source
        # print(html)
        parseHTML(html,sepal_width_arr)
        if file_name != '':
            with open(file_name + f'_{i+1}.html', 'w', encoding='utf-8') as f:
                f.write(html)

    client.quit()
    print(sepal_width_arr)
    print(np.sum(sepal_width_arr))
    return html


def parseHTML(html,sepal_width_arr):
    root = etree.HTML(html)
    trs = root.xpath('//tr')
    for tr in trs:
        tds = tr.xpath('./td')
        if len(tds) > 2:
            sepal_width_arr.append(float(tds[2].text))
    
    


if __name__ == '__main__':
    # example: 1
    # html = getHTML(base_url, './data/c03/c03')

    # example: 2
    sepal_width_arr = []
    for i in range(1, 6):
        random_value = random.randint(2000, 10000)
        timestamp = int(time.time())
        xorResult = i ^ timestamp
        md5_hash = hashlib.md5()
        md5_hash.update(f'{xorResult}{timestamp}'.encode('utf-8'))
        hash = md5_hash.hexdigest()
        payload = {
            'random': random_value,
            'timestamp': timestamp,
            'hash': hash,
            'xorResult': xorResult
        }
        # print(payload)
        json_response = requests.post(base_url, headers=myheaders,json=payload).text

        print(json_response)
        json_data = json.loads(json_response)
        for item in json_data:
            # print(item)
            sepal_width_arr.append(item['sepal_width'])

    print(sepal_width_arr)
    print(np.sum(sepal_width_arr))

