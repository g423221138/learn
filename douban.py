#xpath简易爬虫豆瓣

import requests
from lxml import etree

def getinfo(db):
    r = requests.get(db)

    r.encoding = r.apparent_encoding

    html = etree.HTML(r.text)

    # 片名信息
    title = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')

    # 导演主演信息
    info = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[1]/text()')

    # 评分信息
    rate = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]/text()')

    for i in zip(title, rate):
        print({'title': i[0], 'rate': i[1]})

url = 'https://movie.douban.com/top250?start={}&filter='

for p in range(0,225,25):
    db = url.format(p)
    getinfo(db)

