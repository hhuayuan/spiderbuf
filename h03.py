# coding=utf-8
import os.path

import requests
from lxml import etree
import time

base_url = 'https://www.spiderbuf.cn/playground/h03'

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

def getHTML(url,file_name=''):
    html = requests.get(url, headers=myheaders).text
    if file_name != '':
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(html)
    return html


def downloadImage(url, path=''):
    img_data = requests.get(url, headers=myheaders).content
    # get image file name
    file_name = url.split('/').pop()

    with open(os.path.join(path, file_name), 'wb') as img:
        img.write(img_data)


def parseHTML(html):
    # parse html source code here
    root = etree.HTML(html)
    divs = root.xpath('/html/body/div/div/div[@style="margin-top: 10px;"]')
    i = 1
    for div in divs:
        if i % 2 == 0:
            # 简介 /html/body/div[2] /div[3]/div
            summarys = div.xpath('./div/text()')
            summary = ''
            if len(summarys) > 0:
                summary = summarys[0].strip()
            print(summary)
        else:
            titles = div.xpath('./div/h2')
            title = ''
            if len(titles) > 0:
                title = titles[0].text
                print(title)
            #haibao
            img_urls = div.xpath('./div/div/img/@src')
            img_url = ''
            if len(img_urls) > 0:
                img_url = 'http://spiderbuf.cn/' + img_urls[0]
            print(img_url)
            downloadImage(img_url, './data/h02')
            # 评分 /html/body/div[2]/div[2]  /div/div[2]/span[1]
            ratings = div.xpath('./div/div/span[contains(text(),"豆瓣电影评分:")]/following::text()[1]')
            rating = ''
            if len(ratings) > 0:
                rating = ratings[0].strip()
            print(rating)
            # 导演 /html/body/div[2]/div[2] /div/div[2]/span[2]/span[2]
            directors = div.xpath('./div/div/span/span[contains(text(),"导演")]/following::text()')
            director = ''
            if len(directors) > 1:
                director = directors[1].strip()
            if len(directors) > 3:
                director += '/' + directors[2].strip()
            # for item in directors:
            #     if director != '':
            #         director += ' / '
            #     director += item.text
            print(director)
            # 编剧 /html/body/div[2]/div[2]  /div/div[2]/span[3]/span[2]
            scriptwriters = div.xpath('./div/div/span/span[contains(text(),"编剧")]/following::text()')
            scriptwriter = ''
            if len(scriptwriters) > 0:
                scriptwriter = scriptwriters[1].strip()

            if len(scriptwriters) > 3:
                scriptwriter += scriptwriters[2].strip()
            print(scriptwriter)
            # 主演
            performers = div.xpath('./div/div/span/span[contains(text(),"主演")]/following::text()')
            performer = ''
            if len(performers) > 0:
                performer = performers[1].strip()

            if len(performers) > 3:
                performer += performers[2].strip()
            print(performer)
            # 类型
            genres = div.xpath('./div/div/span/span[contains(text(),"类型:")]/following::text()')
            genre = ''
            if len(genres) > 0:
                genre = genres[0].strip()

            if len(performers) > 1:
                genre += genres[1].strip()
            print(genre)
            # 制片国家/地区
            areas = div.xpath('./div/div/span/span[contains(text(),"制片国家/地区:")]/following::text()')
            area = ''
            if len(areas) > 0:
                area = areas[0].strip()
            print(area)
            # 语言
            langs = div.xpath('./div/div/span/span[contains(text(),"语言:")]/following::text()')
            lang = ''
            if len(langs) > 0:
                lang = langs[0].strip().replace('\n', '')
            if len(langs) > 1:
                lang += langs[1].strip().replace('\n', '')
            print(lang)
            # 又名
            aliases = div.xpath('./div/div/span/span[contains(text(),"又名:")]/following::text()')
            alias = ''
            if len(aliases) > 0:
                alias = aliases[0].strip().replace('\n', '').replace('|', '')
            if len(aliases) > 1:
                alias += aliases[1].strip().replace('\n', '').replace('|', '')
            print(alias)
            # IMDb
            imdbs = div.xpath('./div/div/span[contains(text(),"IMDb:")]/following::text()')
            imdb = ''
            if len(imdbs) > 0:
                imdb = imdbs[0].strip().replace('\n', '')
            print(imdb)
            # 上映日期
            release_dates = div.xpath('./div/div/span/span[contains(text(),"上映日期:")]/following::text()')
            release_date = ''
            if len(release_dates) > 0:
                release_date = release_dates[0].strip().replace('\n', '')
            if len(release_dates) > 1:
                release_date += release_dates[1].strip().replace('\n', '')
            print(release_date)
            # 片长
            runtimes = div.xpath('./div/div/span/span[contains(text(),"片长:")]/following::text()')
            runtime = ''
            if len(runtimes) > 0:
                runtime = runtimes[0].strip().replace('\n', '')
            if len(runtimes) > 1:
                runtime += runtimes[1].strip().replace('\n', '')
            print(runtime)
        i += 1


if __name__ == '__main__':

    html = getHTML(base_url, './data/h03/h03.html')
    # get next page uri
    uri = ''
    root = etree.HTML(html)
    divs = root.xpath('//div[@id="sLaOuol2SM0iFj4d"]/text()')
    if len(divs) > 0:
        uri = divs[0]

    i = 1
    while (uri != '') & (i < 10):
        print(uri)
        html = getHTML(base_url + '/' +  uri, f'./data/h03/h03_{uri}.html')
        uri = '' # ***
        root = etree.HTML(html)
        divs = root.xpath('//div[@id="sLaOuol2SM0iFj4d"]/text()')
        if len(divs) > 0:
            uri = divs[0]
        i += 1

    # parseHTML(html)
