# coding=utf-8
import os.path

import requests
from lxml import etree
import time

base_url = 'https://www.spiderbuf.cn/playground/n04'

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

def getHTML(url,file_name=''):
    html = requests.get(url, headers=myheaders).text
    if file_name != '':
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(html)
    return html



def parseHTML(html):
    class_map = {'abcdef::before':'7',
                'abcdef::after':'5',
                'ghijkl::before':'8',
                'ghijkl::after':'9',
                'mnopqr::before':'9',
                'mnopqr::after':'1',
                'uvwxyz::before':'1',
                'uvwxyz::after':'4',
                'yzabcd::before':'2',
                'yzabcd::after':'6',
                'efghij::before':'3',
                'efghij::after':'2',
                'klmnop::before':'5',
                'klmnop::after':'7',
                'qrstuv::before':'4',
                'qrstuv::after':'3',
                'wxyzab::before':'6',
                'wxyzab::after':'0',
                'cdefgh::before':'0',
                'cdefgh::after':'8',
                'hijklm::after':'6',
                'opqrst::after':'0',
                'uvwxab::after':'3',
                'cdijkl::after':'8',
                'pqrmno::after':'1',
                'stuvwx::after':'4',
                'pkenmc::after':'7',
                'tcwdsk::after':'9',
                'mkrtyu::after':'5',
                'umdrtk::after':'2'}
    # parse html source code here
    root = etree.HTML(html)
    divs = root.xpath('/html/body/div/div[@style="margin-top: 10px;"]')

    for div in divs:
        titles = div.xpath('./div/h2')
        title = ''
        if len(titles) > 0:
            title = titles[0].text
            print(title)
        # 评分
        ranking_spans = div.xpath('./div/div[2]/span[@class]')

        if len(ranking_spans) > 0:
            span = ranking_spans[0]
            attr_class = span.attrib["class"] if "class" in span.attrib else ""
            # print(f"{span} - {attr_class}")
            # print(span.text)

            classes = attr_class.split(" ")
            if len(classes) > 0:
                s1 = class_map[classes[0] + '::before']
                s2 = class_map[classes[1] + '::after']
                print(f'{s1}.{s2}')


if __name__ == '__main__':
    html = getHTML(base_url, './data/n04/n04.html')
    parseHTML(html)
