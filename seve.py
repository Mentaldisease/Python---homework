# 1、使用 ThreadPoolExecutor 和多线程搭配，要求：a). 用一个线程监视当前已完成的进度；
# b).用 ThreadPoolExecutor 创建3个线程执行 fib 函数；c). 用另外一个线程作为生产者

def mo(fn):
    def wrapper(*args,**kwargs):
        import time
        start = time.time()
        rs = fn(*args,**kwargs)
        end = time.time()
        print(end - start)
        print('运行结束')
        return rs
    return wrapper

def product():
    number =  range(25,38)
    yield number

def fib(n):
    n = (yield)
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)


import time
import concurrent.futures import ProcessPoolExecutor
@mo
if __name__ == '__main__':
    start2 = time.time()

    with ProcessPoolExecutor(max_workers=3) as executor:
        for num,result in zip(product(),executor.map(fib,product())):
            print(f"fib{num} = {result}")


# 2、写一个异步生成器，要求：a). 用到 async for，b). 抓取10个”http://httpbin.org/get?a=X"这样的url (X为0-9这十个数字)，并打印a的值
import asyncio
import random

async def product():
    num = random.random(0,10)
    yield num

async def g2():
    async for x in product():
        print(f"http://httpbin.org/get?a={x}")

loop = asyncio.get_event_loop()
try:
    result = loop.run_until_complete(g2())
finally:
    loop.close()