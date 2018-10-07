#1.编写一个函数完成密码生成器的功能，输入参数有密码长度和密码组成的内容，
#  密码组成的内容可以有大写字母（A-Z）、小写字母（a-z）、数字（0-9）、特殊符号（~!@#$%^&*()），
#  返回值为按照用户要求生成的随机密码


def passwd_gen(p_len, lower_case=True, upper_case=True, number=True, special_char=True):
    import string
    import random
    lower_case_set = set(list(string.ascii_lowercase))
    upper_case_set = set(list(string.ascii_uppercase))
    number_set = set([x for x in range(10)])
    special_char_set = set(list('~!@#$%^&*()'))
    user_choice = set()
    if lower_case:
        user_choice = user_choice | lower_case_set
    if upper_case:
        user_choice = user_choice | upper_case_set
    if number:
        user_choice = user_choice | number_set
    if special_char:
        user_choice = user_choice | special_char_set
    passwd_lst = random.sample(user_choice, p_len)
    return ''.join(passwd_lst)

passwd_gen(10)

#2.输入参数为一个整数列表和一个整数，判断该整数是否存在于该列表中。如果存在，是在列表的左半边还是右半边

def judge2(number,lst):
	b=-1
	c=0
	d=[]
	for a in lst:
		if a==number:
			print("列表里有元素%d" %(number))
			c=1
			break
	if c==0:
		print("列表里不存在元素%d" %(number))
	else:
            b = lst.index(number,b+1)
            d.append(b)
            for a in d:
	        if (len(lst) - 1) / 2 > a:
		    print("左边有一个")
		elif (len(lst)-1) / 2 < a:
	            print("右边有一个")
		else:
		    print("正好在中间有一个")

#3.过滤1-100中的素数

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if not n % x:
                return False
        return True

list(filter(is_prime, range(1,101)))

#4.编写一个模块，
#  要求里面有变量x和y，两数相加add(x, y)，两数相减sub(x, y)，两数相乘mul(x, y)，两数相除div(x, y)这四个方法的实现

import demo
add(x,y)
sub(x,y)
mul(x,y)
def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('除数不能为0')

#5.输入参数是一个整数列表，请找出该列表中最小的整数并返回

def get_min_value(lst):
    from functools import reduce
    return reduce(lambda x, y: x if x < y else y, lst)

get_min_value([9,2,3,1,0,2,0.3,12])
          