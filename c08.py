# coding=utf-8

import time
import base64
import hmac
import hashlib
import requests
import urllib.parse
import json
from Crypto.Cipher import AES
import numpy as np

base_url = 'https://spiderbuf.cn/web-scraping-practice/scraper-practice-c08'

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'Referer': base_url}


timestamp = int(time.time())
timestamp_str = str(timestamp)

salt_raw = '{:.6f}'.format(time.perf_counter() * 1000)  # 保留小数，类似浏览器行为
salt = base64.b64encode(salt_raw.encode()).decode()    # 标准 Base64（btoa）

message = (salt + timestamp_str).encode()

digest = hmac.new(base_url.encode(), message, hashlib.sha256).digest()
signature_b64 = base64.b64encode(digest).decode()

# 5a) 方式 A：让 requests 帮你做 URL 编码（通常足够）
params = {'t': timestamp_str, 's': salt, 'sig': signature_b64}
resp = requests.get(base_url + '/api', params=params, headers=myheaders)
print('请求 URL（requests 自动编码）:', resp.url)
print('状态码:', resp.status_code)
print('响应 body:', resp.text)

result = json.loads(resp.text)
key = signature_b64[:16].encode("utf-8")

cipher_data = base64.b64decode(result['d'])

# 前 16 字节是 IV，后面才是密文
iv = cipher_data[:16]
ciphertext = cipher_data[16:]

# AES-CBC 解密
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = cipher.decrypt(ciphertext)

# 去掉 PKCS7 填充
pad_len = decrypted[-1]
decrypted = decrypted[:-pad_len]

# 转成 UTF-8 字符串并解析 JSON
raw = decrypted.decode("utf-8")
items = json.loads(raw)

prices = []
for item in items:
    p = item['price']
    prices.append(p)

print(round(np.average(prices),2))
