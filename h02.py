# coding=utf-8
import os.path

import requests
from lxml import etree
import time

base_url = 'https://www.spiderbuf.cn/playground/h02'

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
    divs = root.xpath('/html/body/div/div[@style="margin-top: 10px;"]')
    i = 1
    for div in divs:
    # <div class ="row" style="margin-top: 10px;">
    #     <div class ="col-xs-12 col-lg-12">
    #         <h2 > 肖申克的救赎 The Shawshank Redemption</h2 ><br>
    #         <div class ="col-xs-3 col-lg-3">
    #             <img src="/static/images/douban_movie/posters/tt0111161.jpg" alt = "肖申克的救赎 The Shawshank Redemption" class="img-responsive img-thumbnail">
    #         </div>
    #         <div class ="col-xs-9 col-lg-9">
    #             <span> 豆瓣电影评分: </span> 9.7<br>
    #             <span> <span> 导演 </span>: <span> 弗兰克·德拉邦特 </span> </span><br>
    #             <span> <span> 编剧 </span>: <span> 弗兰克·德拉邦特 </span> </span>/ 弗兰克·德拉邦特/ 斯蒂芬·金<br>
    #             <span> <span> 主演 </span>: <span> 蒂姆·罗宾斯 </span> </span>/ 蒂姆·罗宾斯/ 摩根·弗里曼/ 鲍勃·冈顿/ 威廉姆·赛德勒/ 克兰西·布朗/ 吉尔·贝罗斯/ 马克·罗斯顿/ 詹姆斯·惠特摩/ 杰弗里·德曼/ 拉里·布兰登伯格/ 尼尔·吉恩托利/ 布赖恩·利比/ 大卫·普罗瓦尔/ 约瑟夫·劳格诺/ 祖德·塞克利拉/ 保罗·麦克兰尼/ 芮妮·布莱恩/ 阿方索·弗里曼/ V·J·福斯特/ 弗兰克·梅德拉诺/ 马克·迈尔斯/ 尼尔·萨默斯/ 耐德·巴拉米/ 布赖恩·戴拉特/ 唐·麦克马纳斯<br>
    #             <span> <span> 类型: </span> <span> 剧情 </span> </span>/ 剧情/ 犯罪<br>
    #             <span> <span> 制片国家/ 地区: </span> <span> 美国 </span> </span><br>
    #             <span> <span> 语言: </span> <span> 英语 </span> </span><br>
    #             <span> <span> 上映日期: </span> <span> 1994 - 09 - 10(多伦多电影节) </span> </span>/ 1994 - 09 - 10(多伦多电影节)/ 1994 - 10 - 14(美国)<br>
    #             <span> <span> 片长: </span> <span> 142分钟 </span> </span><br>
    #             <span> <span> 又名: </span> <span> 月黑高飞(港) </span> </span>/ 月黑高飞(港)/ 刺激1995(台)/ 地狱诺言/ 铁窗岁月/ 消香克的救赎<br>
    #             <span> IMDb: </span> tt0111161<br>
    #         </div>
    #     </div>
    # </div>
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
    html = getHTML(base_url, './data/h02/h02.html')
    # with open('./data/h02/h02.html', 'r', encoding='utf-8') as f:
    #     html = f.read()
    parseHTML(html)
