# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pip._vendor.distlib.compat import raw_input

import math # 等价于 from math import *
import time

'''
print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,。

在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
在函数传参时不会修改其值
'''
def paramPlus(arg1, *args):
    print("show:")
    print(arg1)
    count=arg1
    for i in args:
        print(i)
        count+=i
    return count

paramPlus(1)
sum = lambda arg1, arg2: arg1+arg2 # lambda表达式
print("相加后的值为：",sum(5,paramPlus(1,2,3,4)))

ticks = time.time()
struct_time_8 = time.localtime(ticks)
format_time = time.asctime(struct_time_8)
my_time = time.strftime("%D %H:%M:%S",time.localtime()) #"%Y-%m-%d %H:%M:%S"
'''
python中时间日期格式化符号：

%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00-59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''
print(format_time)
print(my_time)

fo = open("test.txt", "r+")
#fo.write("hello\nwbw\n")
phrase = fo.read(2)  # 读取前两个字
print(phrase)
fo.close()

a = 2
b = a**a #幂运算
s = '123ceds'
list = [12, 'www', '222']
tuple = ('sss', )  #元组元素值不允许修改
diction = {}
diction["key1"] = 'this is one' # 键是字符或数字
diction[2] = 'this is two'

for ch in s:
    print('当前字母：%s'%ch)
print(b+len(list))
print(s[-5:-3])
if b not in list:
    print(tuple[0:])
print(diction)

colors=['red','orange','yellow','green','blue']
i=0
while i<len(colors):
    if(colors[i] == 'purple'): break
    i+=1
else: print('else打印不是正常循环结束')

for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print("%d=%d*%d"%(num, j, i))
            break
    else:print("%d是质数" %num)  # 在循环正常执行完的时候执行else语句

