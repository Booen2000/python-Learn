import requests
from lxml import etree
import re

import json
'''
爬取有规律变化的下一页，获取列表信息
例如：'https://www.dushu.com/book/1001_{}.html'.format(num),
'''

baseurl = 'https://www.dushu.com'

def request(num):
    response = requests.get(
        url='https://www.dushu.com/book/1001_{}.html'.format(num),
        headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}
    )
    page = etree.HTML(response.text)
    return page

def detail(page, current_page):
    item = {}
    lis = page.xpath('//div[@class="bookslist"]/ul/li')
    urls = []
    for li in lis:
        item['name'] = li.xpath('div/h3/a/text()')[0]
        item['author'] = li.xpath('div/p[1]/text()')[0]
        item['description'] = li.xpath('div/p[contains(@class,"disc")]/text()')[0]
        urls.append(li.xpath('div/h3/a/@href')[0])
    print(urls)
    # 每一页的详细url,详细url里面的全部内容
    content = []
    for url in urls:
        response = requests.get(
            url = baseurl + url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}
        )
        page = etree.HTML(response.text)

        name = page.xpath('//div[@class = "book-title"]/h1/text()')[0]
        price = page.xpath('//p[@class = "price"]/span/text()')[0]
        author = page.xpath('//div[@class = "book-details"]/div[1]/table/tbody/tr[1]/td[2]/text()')[0]
        press = page.xpath('//div[@class = "book-details"]/div[1]/table/tbody/tr[2]/td[2]/text()')[0]
        time = page.xpath('//div[@ class="book-details"]/table/tbody/tr[1]/td[4]/text()')[0]
        summary = page.xpath('//div[contains(@class,"txtsummary")]/text()')[0]
        content.append(
            {
                'name': name,
                'price': price,
                'author': author,
                'press': press,
                'time': time,
                'summary': summary
             }
        )

    print(content)
    # 将每一详细页的内容写入当前页面的json中去
    with open('page{}.json'.format(current_page), 'w', encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False)

    '''
    写入乱码的问题：读入的时候用utf-8 , 写入json的时候不检查ascii
    读取json文件时，先按gbk方式对其解码，再编码为utf-8的格式
    data = json_file.read().decode(encoding='gbk').encode(encoding='utf-8')
    result = json.loads(data)
    '''

    '''
             一个一个页面的存，利用对象，可被重写，边取边存
             上面是先取再写
             利用字典存储信息，存储为json格式文件时，会出现乱码
             info = {}
             info['price'] = page.xpath('//p[@class = "price"]/span/text()')[0]
             info['author'] = page.xpath('//div[@class = "book-details"]/div[1]/table/tbody/tr[1]/td[2]/text()')[0]
             info['press'] = page.xpath('//div[@class = "book-details"]/div[1]/table/tbody/tr[2]/td[2]/text()')[0]

             info['time'] = page.xpath('//div[@ class="book-details"]/table/tbody/tr[1]/td[4]/text()')[0]

             info['summary'] = page.xpath('//div[contains(@class,"txtsummary")]/text()')[0]
        '''

def initial():
    # 开始
    page = request(1)
    # 获取当前页面数
    current_page = int(page.xpath('//span[@class = "current"]/text()')[0])
    # 获取是否有下一页面
    is_next = page.xpath('//div[@class = "pages"]/a[last()]/text()')[0]

    while re.match(r'下一页', is_next):
        print(current_page, is_next)

        # 当前页面数据的处理 && 跳转到更详细的页面
        detail(page, current_page)
        # 更新页数
        current_page += 1
        # 对新页面再次发起请求
        page = request(current_page)
        is_next = page.xpath('//div[@class = "pages"]/a[last()]/text()')[0]

    # 最后一页跳出循环，但需要进行相同的存储操作
    detail(page, current_page)

initial()

def test():
    response = requests.get(
        url="https://www.dushu.com/book/13881191/",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}
    )
    page = etree.HTML(response.text)
    info = {}
    info['price'] = page.xpath('//p[@class = "price"]/span/text()')[0]
    print(info['price'])
    info['author'] = page.xpath('//div[@class = "book-details"]/div[1]/table/tbody/tr[1]/td[2]/text()')[0]
    print(info['author'])


