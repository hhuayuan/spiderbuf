# coding=utf-8

import requests
from lxml import etree
from selenium import webdriver


base_url = 'http://www.spiderbuf.cn/h04'

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

def getHTML(url,file_name=''):
    client = webdriver.Chrome()
    client.get(url)
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
    # html = getHTML(base_url, './data/h04/h04.html')
    # parseHTML(html, './data/h04/h04.txt')

    # example: 2
    url = 'http://spiderbuf.cn/static/js/h04/udSL29.js'
    js_code = requests.get(url, headers=myheaders).text
    # js_code = js_code.encode('utf-8').decode('unicode-escape')
    a = js_code.index('=') + 1
    b = js_code.index(';')
    js_code = js_code[a:b]

    # 将字符串转换为字典
    dict_data = eval(js_code)
    print(dict_data)
    for item in dict_data:
        print(item)