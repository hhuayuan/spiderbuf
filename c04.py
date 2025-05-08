# coding=utf-8
# @Author: spiderbuf
from lxml import etree
from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.common.by import By
import time
import random
import numpy as np
import re


base_url = 'https://spiderbuf.cn/web-scraping-practice/scraper-practice-c04'

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.set_capability('goog:loggingPrefs', {'browser': 'ALL'}) 

    options.add_argument('--disable-blink-features=AutomationControlled')  # 改变navigator.webdriver 属性值

    client = webdriver.Chrome(options=options)
    print('Getting page...')
    client.get(base_url)
    time.sleep(3)
    
    # 模拟用户在页面上滑动光标
    actionChains = ActionChains(client)
    actionChains.move_by_offset(430,330)
    for i in range(20):
        step = random.randint(1, 10)
        actionChains.move_by_offset(step,step).perform()

    checkbox = client.find_element(By.ID, 'captcha')
    checkbox.click()
    print('Checkbox clicked...')
    time.sleep(3)
    html = client.page_source
    # print(html)
    client.quit()

    with open('./data/c04/c04.html', 'w', encoding='utf-8') as f:
        f.write(html)

    root = etree.HTML(html)
    items = root.xpath('//div[@class="stats"]')
    results = []
    for item in items:
        spans = item.xpath('.//span')
        s = ''.join(spans[3].xpath('string(.)'))
        results.append(int(re.findall('\d+',spans[0].text)[0]) + int(''.join(re.findall('\d+',s))))

    print(np.average(results))