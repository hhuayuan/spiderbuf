# ESP8266 作为爬虫服务器

## 安装工具

```shell
pip install esptool # 用来刷固件
pip install adafruit-ampy # 用来烧录文件到 ESP8266
```

在 macOS 安装好之后的目录：/Library/Frameworks/Python.framework/Versions/(你实际的Python版本号)/bin

## 下载固件

[MiscroPython](https://micropython.org/download/ESP8266_GENERIC)

[ESP8266_GENERIC-20250415-v1.25.0.bin](https://micropython.org/resources/firmware/ESP8266_GENERIC-20241129-v1.24.1.bin)

## 刷固件
连接ESP8266：

用USB线将ESP8266开发板连接到电脑。
检查串口号（Windows：在设备管理器中查看；Linux/Mac：运行ls /dev/tty*）。

类似 /dev/tty.usbserial-xxxx

```shell
/Library/Frameworks/Python.framework/Versions/(你实际的Python版本号)/bin
```

### 擦除 Flash

```shell
./esptool --port 你的板子所有在的串口 erase_flash
```

类似：
```shell
./esptool --port /dev/tty.usbserial-xxxx erase_flash
```

### 写固件

```shell
./esptool --port 你的板子所有在的串口 --baud 460800 write_flash --flash-size=detect 0x0 你的固件文件目录/ESP8266_GENERIC-20250415-v1.25.0.bin
```

### 验证

```shell
./ampy --port 你的板子所有在的串口 ls
```

## 上传脚本
如果需要在板子通电就执行代码，代码文件名必须是 main.py

```shell
./ampy --port 你的板子所有在的串口 put ~/code/spiderbuf/esp8266/main.py
```


## HTTP 爬虫测试

如果手上没有 HTTP 服务器测试，可以在任意目录下放一个index.html文件，然后在命令行 cd 到这个目录执行：

```shell
python3 -m http.server 8081
```
test.py 文件中的第 17 行的网址就改成 http://你的内网IP地址:8081/index.html
