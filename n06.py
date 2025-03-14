# coding=utf-8
import os.path

import requests
from lxml import etree
import time

base_url = 'https://spiderbuf.cn/web-scraping-practice/scraping-form-rpa'

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

def getHTML(url,file_name=''):
    html_bytes = requests.get(url, headers=myheaders).content
    html = html_bytes.decode()
    if file_name != '':
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(html)
    return html



def parseHTML(html):
    # parse html source code here
    root = etree.HTML(html)
    inputs = root.xpath('//input')

    for input in inputs:
        attr_name = input.attrib['name'] if 'name' in input.attrib else ''
        input_value = input.attrib['value'] if 'value' in input.attrib else ''
        if attr_name == 'username':
            print(f'用户名:{input_value}')

        if attr_name == 'password':
            print(f'密码:{input_value}')

        if attr_name == 'email':
            print(f'邮箱:{input_value}')

        if attr_name == 'website':
            print(f'网站:{input_value}')

        if attr_name == 'date':
            print(f'生日:{input_value}')

        if attr_name == 'time':
            print(f'时间:{input_value}')

        if attr_name == 'number':
            print(f'数量:{input_value}')

        if attr_name == 'range':
            print(f'滑块:{input_value}')

        if attr_name == 'color':
            print(f'颜色:{input_value}')

        if attr_name == 'search':
            print(f'搜索:{input_value}')

        if attr_name == 'gender':
            temp = input.attrib['checked'] if 'checked' in input.attrib else ''
            if temp != '':
                print(f'性别:{input_value}')

        if attr_name == 'interest':
            temp = input.attrib['checked'] if 'checked' in input.attrib else ''
            if temp != '':
                print(f'开发语言:{input_value}')

    options = root.xpath('//select[@name="country"]/option')
    for option in options:
        attr_name = option.attrib['selected'] if 'selected' in option.attrib else ''
        option_value = option.attrib['value'] if 'value' in option.attrib else ''
        if attr_name != '':
            print(f'人物代表:{option_value}')

    lis = root.xpath('//ul[@class="items"]/li/a')
    for li in lis:
        attr_name = li.attrib['class'] if 'class' in li.attrib else ''
        li_value = li.text
        if 'active' in attr_name:
            print(f'代表人物出处：{li_value}')


if __name__ == '__main__':
    html = getHTML(base_url, './data/n06/n06.html')
    parseHTML(html)
