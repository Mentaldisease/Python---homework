#1����дһ����������˷��ھ���ִ�н����ͼ��ʾ����ʾ��print Ĭ�������ỻ�У�����ͨ�� print ���������Ƿ��У� 
for m in range(1, 10):
    for n in range(1, m+1):
        print("%d*%d=%d\t"%(n,m,n*m), end="")
 
    print("")
 
#2����дһ��������������ӡ 1 �� 100��
#��������ܱ�3��������ʾ Fizz��
#��������ܱ� 5 ��������ʾ Buzz��
#�����ͬʱ�� 3 �� 5 ����������ʾ FizzBuzz
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

3����дһ����������� 10 ���ڵ�쳲���������
def fib(x):
    for i in range(11):
        if x <= 1:
            return 1
        return fib(x - 1) + fib(x - 2)
        print(fib(i))

fib(10)
        