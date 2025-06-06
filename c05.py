# coding=utf-8
# @Author: spiderbuf
from selenium import webdriver
import time
import json

base_url = 'https://spiderbuf.cn/web-scraping-practice/scraper-practice-c05'


if __name__ == '__main__':
    client = webdriver.Chrome()
    print('Getting page...')
    client.get(base_url)
    time.sleep(3)
    
    result = client.execute_script('''const bytes = CryptoJS.AES.decrypt(_0x2d8e()[6], _0x2d8e()[31]);
return bytes.toString(CryptoJS.enc.Utf8);''')
    print(result)
    client.quit()

    json_data = json.loads(result)
    total = 0
    i = 0
    for item in json_data["flights"]:
        total += int(item["price"])
        i += 1
    print(total / i)