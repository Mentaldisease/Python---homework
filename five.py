#1、使用偏应用函数实现一个函数求2和其他整数的积
def mul(x,y):
    return x * y

from functools import partial
mul_p = partial(mul,2)
print(mul_p(3))

#2、将柯里化的例子用偏应用函数 partial 实现
def add(x,y,z):
    return x + y + z

add_p = partial(add,1)
print(add_p(2,3))

#3、实现一个装饰器：计时函数从执行开始到执行完毕所花费的时间
def do(fn):
    def wrapper():
        import time
        start = time.time()
        rs = fn()
        end = time.time()
        print(end - start)
        return rs
    return wrapper

@do
def func():
    print('start')
    for x in range(1000):
        print(x)

func()

#4、实现一个装饰器：检查除法函数传入的参数，避免除法函数抛 ZeroDivisionError 异常
def try_div(x,y):
    try:
        rs = x / y
        print(rs)
    except:
        print("除数不为0")
    else:
        return rs

try_div(2,1)
try_div(2,0)

#5、实现一个装饰器：使被装饰的函数在每次执行完毕后打印’Done’和当前时间（精确到秒）
def now_time(fn):
    def wrapper():
        import datetime
        rs = fn()
        print("Done")
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return rs
    return wrapper


@now_time
def func():
    print('start')
    for x in range(10):
        print(x)

func()