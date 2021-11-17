import time
import string
from functools import reduce
from sys import stdout
import random
from inspect import isgeneratorfunction #判断
# 函数可复用性，返回list，不要直接print

'''
函数可复用性，返回list，不要直接print，可使用yield迭代器
yield:
yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
    Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！
简要理解：yield就是 return 返回一个值(不结束)，并且记住这个返回的位置，下次迭代就从这个位置后开始。
'''

def read_file(fpath):
    block_size = 1024
    with open(fpath,'rb') as f:
        while True:
            block = f.read(block_size)
            if block:
                yield block
            else:
                return


'''
如果直接对文件对象调用 read() 方法，会导致不可预测的内存占用。
好的方法是利用固定长度的缓冲区来不断读取文件内容。通过 yield
for i in read_file('1.txt'):
    print(i)

'''


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用 yield
        # print b
        a, b = b, a + b
        n = n + 1

# print(next(fab(5)))

def yield_Test(n):
    for i in range(n):
        yield call(i)
        print("内部i：",i)
    print("sss")

def call(i):
    return i*2
'''
for i in yield_Test(5):
    print(i)
    pass
'''

def input_test():
    def input_string():
        s = input("请输入字符串: ")
        with open('1.txt', 'w') as f:
            s = s.upper()
            f.write(s)
        # print(f.read())
    input_string()
    with open('1.txt', 'r') as fr:
        print(fr.read())

def input_cease():
    filename = input("请输入文件名：")
    with open(filename,"w") as f:
        ch = input("请输入字符串:")
        while(ch != 'exit'):
            f.write(ch)
            ch = input("")

def duration():
    start = time.time()
    for i in range(3000):
        print(i)
    ed = time.time()
    print(ed-start)

# 在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
def jiami():
    a = int(input("请输入一个四位数: "))
    an = []
    an.append(a%10)
    an.append(int(a % 100/10))
    an.append(int(a % 1000/100))
    an.append(int(a / 1000))

    for i in range(4):
        an[i] += 5
        an[i] = an[i]%10
    for i in range(2):
        an[i],an[3-i] = an[3-i], an[i]
    for i in range(3,-1,-1):
        print(an[i], end="")

#读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
def loopAndhint():
    for i in range(7):
        a = int(input("enter a number: "))
        while a < 10 or a > 50 :
            if a == 0:
                break
            a = int(input("enter a number(1-50): "))
        if a == 0:
            print("程序提前退出，goodbye!")
            break
        print("*" * a)


# 输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
def nine_nine():
    a = int(input("请输入一个奇数: "))
    start = 9
    base = 9
    i=1
    begintime = time.time()
    while start % a != 0:
        base = base * 10
        start+=base
        i+=1
        endtime = time.time()
        if endtime - begintime > 0.01:
            break
    if start%a !=0:
        print("数字太大已经到了%d" %start)
    else:
        result = start/a
        print("%d个9可以整除%d" %(i, a))
        print("%d / %d = %d" %(start, a, result))

def transfer():
    n = 0
    p = input("Please input a octal number：") # 八进制数
    for i in range(len(p)):
        n += int(p[len(p)-i-1])*(8**i)
        # n= n*8 + ord(p[i]) - ord('0')
    print(n)

def Peach(n):
    '''
    不考虑桃子为整数，直接从最小开始
    min = 4
    i = 0
    while i<5:
        x2 = min/4*5 + 1
        min = x2
        i += 1
    print(min)
    '''
    # 海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
    # 必须保证整数,四次的rest都能被整除，否则就更换begin
    if n==1:
        count = 0
        # i确定起始数字,也是剩余数目，count是总拿取次数
        for i in range(10000):
            i = i*4
            count = 0
            for j in range(5):
                peach = i/4*5 +1
                i = peach
                if(peach%4 == 0):
                    count+=1
                else: break
            if count==4 :
                print("桃子总数为:",peach)
                break
    elif n ==2:
        #将count 和 i 合并
        times = 0
        j = 1
        while times < 5 :
            x= 4*j
            for times in range(5):
                if x%4 ==0:
                    x = x/4*5 + 1
                    times+=1
                else: break
            j+=1
        print(x)

def searchOldest():
    person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
    m = 'li'
    for key in person.keys():
        if person[m] < person[key]:
            m = key
    print('%s,%d' % (m, person[m]))

def cicleMove():
    n = int(input("请输入总人数："))
    per = []
    for i in range(n):
        per.append(i+1) # 从1开始赋值，0用于标记

    i = 0 # 用于递增，检索
    k = 0 # 三次一更新num[i]和m
    m = 0 # 被淘汰的人数
    while m < n-1:
        if per[i] != 0: k+=1
        if k == 3:
            per[i] = 0 # 标记淘汰
            m += 1 # 淘汰的人加1
            k = 0 # 重新循环3
        i += 1
        if i == n: i = 0 # 重新开始检索
    # 检验结果
    for i in range(n):
        if per[i] != 0:
            print(per[i])
            break

def loopMove(n,m,s):
    # n为数目，m为要移动的数,s为选择左移或右移
    array=[]
    print("一共有%d个数要输入"%n)
    for i in range(n):
        array.append( int(input("请输入一个数字:")) )
    print("原始：", array)
    for j in range(m): # 移动位数
        if s=='left':
            # 循环左移
            array_begin = array[0]
            for i in range(0,len(array)-1,1):
                array[i] = array[i+1]
            array[len(array)-1] = array_begin
        elif s == 'right':
            # 循环右移
            array_end = array[len(array) - 1]
            for i in range(len(array) - 1, -1, -1):
                array[i] = array[i - 1]
            array[0] = array_end
    print("经过%d位的循环%s移" %(m, s), array)

'''
random函数的使用
print random.random()           #输入0-1之间的随机数
print random.uniform(10,20)     #输出10-20之间的随机数
print random.randint(10,20)     #输出10-20之间的随机整数
'''

#输出1-99间的随机数 x = random.choice([x for x in range(1,100)])


# 求输入数字的平方，如果平方运算后小于 50 则退出。
def loop():
    a = int(input("请输入一个数字:"))
    while a**2>=50:
        print("在循环中")
        a=int(input("请再输入一个数字:"))
        if a**2 <50:
            print("退出循环")
            break
    print("已经退出")

def insert():
    l=[1,22,33,44,53]
    print("原始",l)
    new = int(input("请输入一个数字: "))
    if new >= l[len(l)-1]: l.append(new)
    for i in range(len(l)):
        if l[i]>new: #要插入的位置就是i
            temp = l[i]
            l[i] = new
            l.append(0)
            for j in range(i+1, len(l)):
                temp2 = l[j]
                l[j] = temp
                temp = temp2
            break
    print("插入后",l)

def matrixAdd():
    x = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]

    y = [[5, 8, 1],
         [6, 7, 3],
         [4, 5, 9]]

    z = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # 初始化
    for i in range(3):
        # z.append([])
        for j in range(3):
            z[i][j] = x[i][j] + y[i][j]
    print(z)

def matrix():
    l =[]
    sum = 0.0
    print("请创建矩阵:")
    for i in range(3):
        l.append([])
        for j in range(3):
            print("第 %d 行"%(i+1),end='')
            l[i].append(float(input("：请输入数字：")))
    for i in range(3):
        sum += l[i][i]
    print(sum)

def reorder():
    l=[1,432,2,123,13,647,436]
    # l.sort()
    for i in range(len(l)):
      #  min = l[i]
        for j in range(i+1,len(l)):
            if l[j]<l[i]:
                #min = l[j]
                l[i],l[j]=l[j],l[i]

#a[i:j:s],s表示步数
# a[::-2]
# 当s<0时，i缺省时，默认为-1. j缺省时，默认为-len(a)-1
# 所以a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍，即倒序。
def age(times):
    if times == 1 : c=10
    else:
        c= age(times-1)+2
    return c

def testReverse():
    def reverse(s, index):
        if index == 0:
            return
        print(s[index-1], end='')
        reverse(s, index-1)
    s = input("Please enter a string: ")
    length = len(s)
    reverse(s, length)

def digui(i):
    if i == 0:
        t =1
    else:
        t = i*digui(i-1)
    return t

# 累乘，利用map函数
# map()函数不改变原有的 list，而是返回一个新的 list。
def multiples():
    l= range(1,21)
    def op(x):
        r=1
        for i in range(1,x+1):
            r*=i
        return r
    s = sum(map(op, l))
    print(s)

scientists =({'name':'Alan Turing', 'age':105, 'gender':'male'},
               {'name':'Dennis Ritchie', 'age':76, 'gender':'male'},
               {'name':'Ada Lovelace', 'age':202, 'gender':'female'},
               {'name':'Frances E. Allen', 'age':84, 'gender':'female'})
def reducer(accumulator , value):
     sum = accumulator + value['age'] # 需要原始初值
     return sum

def group_by_gender(accumulator, value):
    accumulator[value['gender']].append(value['name'])
    return accumulator

def testReduce(n):
    if n=='sum':
        total_age = reduce(reducer, scientists, 0) # 从0开始，固定int类型，可有可无的参数
        print(total_age)
        print(sum(x['age'] for x in scientists))
    elif n=='group':
        grouped = reduce(group_by_gender, scientists, {'male':[], 'female':[]})
        print(grouped)

#分数规律，有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
def regular(n):
    if n ==1:
        a1 = 2
        a2 = 3
        b1 = 1
        b2 = 2
        s = a1 / b1 + a2 / b2
        for n in range(18):
            a1,a2 = a2,a1+a2 # 先计算等式右边的值,相当于temp_a=a2  a2=a1+a2  a1=temp_a
            b1,b2 = b2,b1+b2
            s+=a2/b2
        print(s)
    elif n==2:
        a=2
        b=1
        l=[]
        l.append(a/b)
        for n in range(1,20):
            b,a=a,a+b
            l.append(a/b)
        s = reduce((lambda x,y:x+y),l) # reduce the sequence to a single value
        print(s)

# 打印菱形
def rhombus():
    for i in range(4):
        for j in range(2-i+1):
            print(" ",end='')
           # stdout.write(' ')
        for k in range(2*i+1):
            #stdout.write('*')
            print("*", end='')
        print()

# a说他不和x比，c说他不和x,z比
# !!!!!!!!!判断语句
# ord('a')  chr(97):"A"
def battle():
    jia = {'a':'0', 'b':'0', 'c':'0'}
    yi = {'x': '0', 'y': '0', 'z': '0'}
    for i in jia:
        for j in yi:
         #   if yi[j] == '0': # 防止被覆写，为空才寻找对手
            yi[j] = i
            if j == 'x' and i == 'a' and yi[j] == 'a':
                yi[j]='0'
            if j == 'z' and i == 'c' and yi[j] == 'c':
                yi[j]='0'
            if j == 'x' and i == 'c' and yi[j] == 'c':
                yi[j]='0'
    print(yi)

# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
def freeFall():
    height =100
    times =10
    Sn = []
    i=1
    sum=0
    while i<=times:
        if i==1 :
            sum = height
        else:
            sum+=height*2
        height = height/2
        Sn.append(height)
        i+=1
    print(sum,Sn)

# 累加和：如2+22+222+2...2
def defineSum():
    a = int(input("参数："))
    n = int(input("个数："))
    Sum =0
    Tn =0
    for i in range(n):
        Tn = Tn+a;
        Sum += Tn
        a = a*10
    print(Sum)

#引用string库的方法
def count(s):
    letter = 0
    space = 0
    digit = 0
    others = 0
    for c in s:
        if c.isalpha():
            letter+=1
        elif c.isspace():
            space+=1
        elif c.isdigit():
            digit+=1
        else: others+=1
    print("Letters:%d\t Space:%d\t Digit:%d\t Others:%d" %(letter,space,digit,others))

# 正整数分解质因数
def reduceNum(n):
    # 从2-n，从小开始找，找因数的个数
    Sn = []
    print("%d="%n,end='')
    for i in (2,n+1):
        while n!=i:
            if(n%i == 0):
                print('%d*'%i,end='')
                Sn.append(i)
                n=n/i
            else: break
    print("%d*1"%n)
    Sn.append(int(n))
    Sn.append(1)
    return Sn

# 6=1*2*3=1+2+3
def WanShun():
    for i in range(2,1001):
        Sn = reduceNum(i)
        sum = 0
        for j in Sn:
            sum+=j
        if( i== sum): print("*****wanshu:",i)


def DelaySleep():
    myDay = {1:'me', 2:'you'}
    for key in myDay:
        print(key,myDay[key])
        time.sleep(1) # 暂停一秒

# 素数标记
def CountSuShu(a,b):
    sum = 0
    flag = 1 # 素数标记
    for i in range(a,b+1):
        for j in range(2,i):
            if i%j == 0: # 不是素数
                flag=0
                break;
        if flag ==1:
            print("%d" %i)
            sum+=1
        flag =1
               # break
    print(sum)

# 水仙花数
def ShuiXianHua():
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                if i**3+j**3+k**3 == i+10*j+100*k and k!=0:
                    print(k,j,i)

# 打印九九乘法表
def multiplicationTable():
    for i in range(1, 10):
        print()
        for j in range(1, i + 1):
            print("%d*%d=%d " % (i, j, i * j), end="")

