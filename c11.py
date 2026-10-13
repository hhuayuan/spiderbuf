import base64
import hashlib
import hmac
import time
from urllib.parse import quote

import requests


BASE_URL = "https://spiderbuf.cn"
API_URL = BASE_URL + "/challenge/scraper-practice-js-reverse-c11/api"


def generate_signature(chip: str, currency: str, memory: str, timestamp: int) -> str:
    # 完整代码请阅读教程全文
    return ""


def crawl(chip: str = "M4", currency: str = "USD", memory: str = "16GB") -> dict:
    session = requests.Session()

    # 使用秒级时间戳
    timestamp = int(time.time())

    # 生成签名
    signature = generate_signature(chip=chip, currency=currency, memory=memory, timestamp=timestamp)

    # 对应浏览器中的 Cookie：
    # document.cookie = timestamp + "=" +
    #     encodeURIComponent(signature) + ";expires=..."
    session.cookies.set(str(timestamp), quote(signature, safe=""))

    # 根据浏览器实际请求构造查询参数
    params = {
        "chip": chip,
        "currency": currency,
        "memory": memory,
        "t": timestamp,
        "tt": timestamp,
        "s": signature,
    }

    response = session.get(
        API_URL,
        params=params,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/154.0.0.0 Safari/537.36"
            ),
            "Referer": BASE_URL
            + "/challenge/scraper-practice-js-reverse-c11",
        },
        timeout=15,
    )
    print(response.text)
    response.raise_for_status()

    print("请求 URL：", response.url)
    print("HTTP 状态码：", response.status_code)

    return response.json()


if __name__ == "__main__":
    currencies = ["USD","EUR"]
    memories = ["16GB","24GB"]
    total_price = 0
    try:
        for currency in currencies:
            for memory in memories:
                result = crawl(chip="M4", currency=currency, memory=memory)
                print(result)
                total_price = total_price + sum(item["price"] for item in result)

        print("价格总和：", total_price)
    except requests.RequestException as exc:
        print(f"请求失败：{exc}")
    except ValueError as exc:
        print(f"响应不是有效 JSON：{exc}")
