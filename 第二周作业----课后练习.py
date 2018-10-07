#1、编写一个函数输出乘法口诀表，执行结果如图所示（提示：print 默认输出后会换行，可以通过 print 参数控制是否换行） 
for m in range(1, 10):
    for n in range(1, m+1):
        print("%d*%d=%d\t"%(n,m,n*m), end="")
 
    print("")
 
#2、编写一个函数遍历并打印 1 到 100，
#如果数字能被3整除，显示 Fizz；
#如果数字能被 5 整除，显示 Buzz；
#如果能同时被 3 和 5 整除，就显示 FizzBuzz
def sumStartToEnd():
    for i in range(0,101):
        print(i)
            if i%3 == 0:      
                print('Fizz')
	    elif i%5 == 0:
	        print('Buzz')
	    elif i%3 == 0 and i%5 == 0:
	        print('FizzBuzz')

sumStartToEnd()

3、编写一个函数，输出 10 以内的斐波那契数列
def fib(x):
    for i in range(11):
        if x <= 1:
            return 1
        return fib(x - 1) + fib(x - 2)
        print(fib(i))

fib(10)
        