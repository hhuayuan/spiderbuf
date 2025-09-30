import network
import urequests
import ure
import time
import os

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Your WIFI SSID", "Your WIFI Password")

while not sta_if.isconnected():
    time.sleep(1)

print("Wi-Fi已连接，IP地址：", sta_if.ifconfig())

# HTTP GET请求
response = urequests.get("http://example.com")
html = response.text
response.close()
# 提取<tbody>中的<td>
tbody_pattern = r"<tbody>(.*)</tbody>"
tr_pattern = r"<tr>(.*)</tr>"
td_pattern = r"<td>([^<]*)</td>"  # Match simple <td> content

tbody_match = ure.search(tbody_pattern, html)
if tbody_match:
    tbody_content = tbody_match.group(1)
    print("Found <tbody>")

    tr_matches = ure.findall(tr_pattern, tbody_content)
    for tr in tr_matches:
        td_matches = ure.findall(td_pattern, tr)
        for td in td_matches:
            print("  <td>:", td)
            led.off()
            time.sleep(0.5)
            led.on()
            time.sleep(0.5)
else:
    print("No <tbody> found")
