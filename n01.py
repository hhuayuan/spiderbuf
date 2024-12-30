# coding=utf-8

import requests
from lxml import etree

url = 'http://www.spiderbuf.cn/playground/n01'

myheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
             'Referer':'https://spiderbuf.cn/list'}

html = requests.get(url, headers=myheaders).text
print(html)
# < div class ="container" >
# < div class ="row" style="margin-top: 30px" >
# < div class ="col-xs-6 col-lg-4" style="margin-bottom: 30px;" >
# < h2 > 腾讯控股 < / h2 >
# < p > 排名：1 < / p >
# < p > 企业估值(亿元)：39000 < / p >
# < p > CEO：马化腾 < / p >
# < p > 行业：互联网服务 < / p >
# < / div > <!-- /.col - xs - 6.col - lg - 4 -->
f = open('./data/n01/n01.html', 'w', encoding='utf-8')
f.write(html)
f.close()

root = etree.HTML(html)
ls = root.xpath('//div[@class ="container"]/div/div')
# page_text = ls[0].xpath('string(.)')
# print(page_text)

f = open('./data/n01/n01.txt', 'w', encoding='utf-8')
for item in ls:
    hnodes = item.xpath('./h2')
    s0 = hnodes[0].text

    pnodes = item.xpath('./p')
    s1 = pnodes[0].text
    s2 = pnodes[1].text
    s3 = pnodes[2].text
    s4 = pnodes[3].text
    # 富邦金融控股排名：50企业估值(亿元)：2135CEO：蔡明兴行业：金融服务
    s = s0 + '|' + s1.replace('排名：','') + '|' + s2.replace('企业估值(亿元)：','') + '|' \
        + s3.replace('CEO：','') + '|' + s4.replace('行业：','') + '\n'
    print(s)
    f.write(s)
    # s = ''
    # for td in tds:
    #     s = s + str(td.xpath('string(.)')) + '|'
    #     # s = s + str(td.text) + '|'
    # print(s)
    # if s != '':
    #     f.write(s + '\n')

f.close()