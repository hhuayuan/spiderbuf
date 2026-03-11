# coding=utf-8
import base64
import hashlib
import hmac
import time

import requests

session = requests.Session()

URL = "https://spiderbuf.cn/web-scraping-practice/scraper-practice-c09"
# 在浏览器控制台 console.log(getFingerprint()); 拿到一个固定的浏览器指纹
FINGERPRINT = "d579d7027e619e9c7d02117053e67b16cdad9b31b163f6b26f88ea7971ab754d"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"


def get_token():
    """访问页面获取 cookie _token_c09"""
    headers = {
        "User-Agent": USER_AGENT,
    }
    r = session.get(URL, headers=headers)
    if r.status_code != 200:
        raise Exception("status code not 200")

    cookies = session.cookies.get_dict()
    if "_token_c09" not in cookies:
        raise Exception("token not found")

    return cookies["_token_c09"]


def generate_sign(fp, tt, token):
    """
    详见公众号全文教程
    """
    pass
    


def fetch_data(fp, tt, s, token):
    payload = {"tt": tt, "s": s}

    headers = {
        "X-Client-Id": fp,
        "Content-Type": "application/json",
        "User-Agent": USER_AGENT,
    }
    cookies = {"_token_c09": token}
    r = session.post(URL, json=payload, headers=headers, cookies=cookies)
    print(r.text)
    return r.json()


def decode_cpc(item):
    """解密 CPC"""
    """详见公众号全文教程"""
    pass


def main():
    # 1 获取 token
    token = get_token()

    # 2 时间戳
    tt = int(time.time())

    # 3 签名
    s = generate_sign(FINGERPRINT, tt, token)

    # 4 请求数据
    data = fetch_data(FINGERPRINT, tt, s, token)

    cpc_list = []

    for item in data:
        cpc = decode_cpc(item)

        cpc_list.append(cpc)

        print(item["keyword"], "CPC:", cpc, "Monthly:", item["monthly_search_volume"])

    avg = sum(cpc_list) / len(cpc_list)

    print("\nAverage CPC:", avg)


if __name__ == "__main__":
    main()
