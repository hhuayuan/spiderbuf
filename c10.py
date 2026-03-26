import hashlib

import requests
from lxml import etree


class C10Spider:
    def __init__(self):
        self.session = requests.Session()
        self.url = (
            "https://spiderbuf.cn/web-scraping-practice/scraper-practice-js-reverse-c10"
        )
        self.jsluid = ""
        self.clearance = ""

    def get_jsluid(self):
        """
        访问页面获取 __jsluid_h
        """
        _ = self.session.get(
            self.url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
            },
            allow_redirects=False,
        )

        if "__jsluid_h" not in self.session.cookies:
            raise Exception("未获取到 __jsluid_h")

        jsluid = self.session.cookies.get("__jsluid_h")
        return jsluid

    def build_clearance(self, jsluid):
        # 生成 __jsl_clearance
        pass

    def fetch_data(self):
        """
        带 cookie 请求真实页面
        """
        # self.session.cookies.set()对域名要求严格容易因为细节出错，所以在 headers 中设置 cookie 是最稳也是最省事的
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
            "Cookie": f"__jsluid_h={self.jsluid}; __jsl_clearance={self.clearance}",
        }
        resp = self.session.get(self.url, headers=headers)
        if resp.status_code != 200:
            raise Exception(f"请求失败: {resp.status_code}")

        return resp.text

    def parse_data(self, html):
        # 解析 HTML
        parser = etree.HTMLParser()
        tree = etree.fromstring(html, parser)

        # XPath 获取 tbody 下所有 tr
        rows = tree.xpath("//tbody/tr")

        cpc_sum = 0.0

        for row in rows:
            cpc_text = row.xpath("./td[2]/text()")  # 第二列 CPC
            source_text = row.xpath("./td[6]/text()")  # 第六列 Source
            if cpc_text and source_text:
                cpc = float(cpc_text[0].strip())
                source = source_text[0].strip()
                if source in ("Ahrefs", "SEMrush"):
                    cpc_sum += cpc

        print("Ahrefs + SEMrush CPC 列总和:", cpc_sum)

    def run(self):
        # Step1: 获取 jsluid
        self.jsluid = self.get_jsluid()

        # Step2: 构造 clearance
        self.clearance = self.build_clearance(self.jsluid)

        # Step3: 获取数据
        html = self.fetch_data()

        # Step4: 解析数据
        self.parse_data(html)
        # print(html[:500])  # 只打印前500字符


if __name__ == "__main__":
    spider = C10Spider()
    spider.run()
