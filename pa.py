import requests
from lxml import etree
from bs4 import BeautifulSoup

import re


res = requests.get(' https://movie.douban.com/',
                   headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"})

# root = etree.Element(res)
html = etree.HTML(res.text); # 只是一个tag，文档
result = etree.tostring(html, encoding='utf-8') #转换为字节类型

# 从HTML文件提取数据
# 方法一，通过xpath寻找tag
# 将数据写入文件，以备xpath
#with open('C:\Users\87936\Pycharm\project_11_3\venv\t','w') as f:
#    f.write(result)

html_data = html.xpath('//li[@class="title"]/a/text()')


# 方法二：通过BeautifulSoup寻找tag

soup = BeautifulSoup(result)

'''
format的使用例子
for i in range(1,5):
    print("https://market.douban.com/book/?type=topic&page={}".format(i))

urls = ['https://movie.douban.com/top250?start={}&filter='.format(i) for i in range(0,250,25)]
print(urls)

'''


baseurl = 'https://market.douban.com'

response = requests.get(
    url='https://www.dushu.com/book/1001.html',
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}
)
page = etree.HTML(response.text)
print(page.xpath('//a/text()'))

def request(num):
    response = requests.get(
        url='https://market.douban.com/book/?type=topic&page={}&page_num=18&'.format(num),
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}
    )
    page = etree.HTML(response.text)
    return page

def Initial():
    page = request(1)
    print(page.xpath('//a[@class=current]'))
    is_next_page = page.xpath("/html/body/div[3]/div[4]")
    # 找不到后一页！！
    print(is_next_page)
    while is_next_page:
        # 这里做页面的数据处理
        current = page.xpath("//*[@id='paginator']/a[@class='current']/text()")
        request(current+1)


# 方法二：通过BeautifulSoup寻找tag

#soup = BeautifulSoup(result)

def childTest(soup):
    print(soup.li.contents[1].contents)  # contents[0]是\n，contents包含\n
    print(soup.ul)
    #print(soup.ul.descendants)
    for child in soup.ul.descendants:
        print(child)
    '''
    对比soup.ul和soup.ul.contents
     ul:展示的是html格式，contents以列表格式输出
     children也是结点html格式

    对比children和descendants
     .contents 和 .children 属性仅包含tag的直接子节点
      .descendants 属性可以对所有tag的子孙节点进行递归循环（包含字符串）

    .string方法
    如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None :
    .strings 
    .stripped_strings 可以去除多余空白内容
    '''

def parentTest(soup):
    for i in soup.li.a.parents:
        if i is None:
            print(i)
        else:
            print(i.name)

def siblingTest(soup):
    sibling_soup = soup.li
    # print(sibling_soup.next_sibling.next_sibling)
    # 实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白
    # 第一个nextSibling是顿号和换行符
    for sibling in sibling_soup.next_siblings:
        print(sibling)

def elementTest(soup):
    '''
    .next_element 属性指向解析过程中下一个被解析的对象(字符串或tag) 往里外走，再往上下走
    .next_sibling 往上下走
    :param soup:
    :return:
     print(soup.li)
    print(soup.li.a.next_sibling,1)
    print(soup.li.a.next_element,2)
    '''
    for element in soup.li.a.next_elements:
        print(element)

def has_class(tag):
    # 定义一个方法，寻找符合标签
   #  if tag['class'] == 'order':
    return tag.has_attr('class')
           # 错误写法：and tag['class'] == 'order'

# 通过一个方法来过滤一类 标签属性 的时候, 这个方法的参数是要被过滤的属性的值, 而不是这个标签
def not_somewhat(href):
    return href and not re.compile("trailer").search(href)

def filter(soup):
    '''
    find_all( name , attrs , recursive , string , **kwargs )
        name:标签名
        attrs: 类似id='link2'
              attrs={"data-foo": "value"} 不是关键字的，设置字典参数

    '''

    # 1、传入正则表达式
    for tag in soup.find_all(re.compile('h')):
        print(tag.name)

    # 2、传入方法
    one = soup.find_all(has_class)

    # 传入方法2.0
    two = soup.find_all(href=not_somewhat)

    # 解析入参

    three = soup.find_all("a", attrs={'href': re.compile("douban"),'class':'nav-login'}) # 同时过滤tag和属性
    four = soup.find_all('a', class_='',limit=4)
    five = soup.find_all('a', string='第一炉香')

    # recursive参数
    # 如果只想搜索tag的直接子节点,可以使用参数 recursive=False .

   # print(three)
   # print(five)
def findTest(soup):

    '''
    find() 方法直接返回结果.
    find_all() 方法没有找到目标是返回空列表, find() 方法找不到目标时,返回 None .

    '''

def cssTest(soup):
    test = soup.select("head title") # 返回的是列表，不是直接tag
    test[0]['id'] = 1
    del test[0]['id']
    test[0].string = 'wubw'
    print(test)


