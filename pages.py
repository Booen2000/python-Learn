import requests
from lxml import etree
import re

'''
爬取有规律变化的下一页，获取列表信息
例如：'https://www.dushu.com/book/1001_{}.html'.format(num),
'''

baseurl = 'https://www.dushu.com/book'

def request(num):
    response = requests.get(
        url = 'https://www.dushu.com/book/1001_{}.html'.format(num),
        headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}

    )
    page = etree.HTML(response.text)
    return page

def store(page):
    item = {}
    lis = page.xpath('//div[@class="bookslist"]/ul/li')

    for li in lis:
        item['name'] = li.xpath('div/h3/a/text()')[0]
        item['author'] = li.xpath('div/p[1]/text()')[0]
        item['description'] = li.xpath('div/p[contains(@class,"disc")]/text()')[0]
        print(item)
        # 这里做存储操作

def initial():
    # 开始
    page = request(1)
    # 获取当前页面数
    current_page = int(page.xpath('//span[@class = "current"]/text()')[0])
    # 获取是否有下一页面
    is_next = page.xpath('//div[@class = "pages"]/a[last()]/text()')[0]

    while re.match(r'下一页', is_next):
        print(current_page, is_next)

        store(page)

        # 更新页数
        current_page += 1
        # 对新页面再次发起请求
        page = request(current_page)
        is_next = page.xpath('//div[@class = "pages"]/a[last()]/text()')[0]

    # 最后一页跳出循环，但需要进行相同的存储操作
    store(page)
initial()

