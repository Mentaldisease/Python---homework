#1、实现一个装饰器：检查被装饰的函数所传入的参数，如果是字符串类型，且含有小写字母，则将小写字母全部转为大写字母
def wrap(fn):
    def wrapper(str):
        rs = fn(str.upper())
        print(rs)
        return rs
    return wrapper

@wrap
def str_upper(str):
    return str

str_upper('asjdfasA')
#2、实现一个生成器函数：读取文件时每次只返回固定的长度，此长度可由用户调用时设置
def read_file():
    user_in = int(input("请输入读取长度:"))
    x = 0
    while x <= user_in:
        if x == user_in:
            with open('demo.py','r') as f:
                str = f.read()
                print (str[0:x])

        x += 1


read_file()
#3、实现一个生成器函数：模拟数据库中的主键自增，即生成的值为主键自增的结果

#4、实现一个生成器表达式：生成 50 以内的偶数，并用 for 循环打印出每个值
n = (i for i in range(50) if i % 2 == 0)
for i in n:
    print(i)

#5、实现一个生成器函数：读取操作系统 C 盘中的所有文件的名字
import os
from os.path import join, getsize

for root, dirs, files in os.walk("c:\\"):
    fsum = 0
    for name in files:
        fname = join(root, name)
        fsize = getsize(fname)
        fsum += fsize
        print("%s => %d" % (fname, fsize))
    print("%s => %d" % (root, fsize))