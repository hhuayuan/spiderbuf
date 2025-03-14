# coding=utf-8

import requests
from lxml import etree
import numpy as np

base_url = 'https://spiderbuf.cn/web-scraping-practice/scraper-practice-c01/mnist'

my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'Referer': 'https://spiderbuf.cn/web-scraping-practice/c01',
    'Cookie': '__cgf3t=G0gzgFKDRlLtmZH7NrzqOb1x4pek1xNQk12KKc4g21Y-1731624199;'}


html_bytes = requests.get(base_url, headers=my_headers).content
html = html_bytes.decode()
root = etree.HTML(html)
with open('./data/c01/c01.html', 'w', encoding='utf-8') as f:
    f.write(html)
# print(html)

trs = root.xpath('//tbody/tr')


pix1_arry = []
for tr in trs:
    tds = tr.xpath('td')
    # 把 pix1 列的值添加到数组
    pix1_arry.append([int(tds[1].text) if len(tds) > 1 else 0])
# 计算 pix1 列的平均值并四舍五入至两位小数
print(round(np.mean(pix1_arry),2))