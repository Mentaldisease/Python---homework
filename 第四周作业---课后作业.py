#1����дһ��Animal�࣬������name��������call()��
#����Dog���Cat��̳�Animal�࣬�����ʵ�������дcall() �����磬���п��Դ�ӡ������è�п��Դ�ӡ������

class Animal():
    name = ''
    def call():
        print('super Animal')

class Dog(Animal):
    def call():
        print("wang wang")

class Cat(Animal):
    def call():
        print("maio miao")


#2��ʹ�õݹ�ʵ��10���ڵ�쳲���������

def fib(x):
    if x <= 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

#3��ʹ���б��Ƶ���ȡ100���ڵ�����

lst = [print(i) for i in range(0,101)if i % 2 == 1]

#4��ʹ���쳣����ṹʵ�� add(x,y) / sub(x,y) / mul(x,y) / div(x,y)

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

import pdb
def test():
    try:
        print("try")
        print(add(10,0))
        print(sub(10,0))
        print(mul(10,0))
        print(div(10,0))
    except:
        print(sys.exc_info())

#5����Python֮����import this��д���ļ�����ͳ���ж��ٵ��ʼ�����ֵĴ�������ͳ�ƽ�����л����ļ��б���

import json

