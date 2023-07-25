# coding=utf-8

import requests
import json

url = 'http://spiderbuf.cn/iplist?order=asc'

myheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

data_json = requests.get(url, headers=myheaders).text
print(data_json)

f = open('./data/7/07.html', 'w', encoding='utf-8')
f.write(data_json)
f.close()

ls = json.loads(data_json)
print(ls)

f = open('./data/7/data07.txt', 'w', encoding='utf-8')
for item in ls:
    # print(item)
    s = '%s|%s|%s|%s|%s|%s|%s\n' % (item['ip'], item['mac'],item['manufacturer'], item['name'],item['ports'], item['status'], item['type'])
    f.write(s)
f.close()