#1.��дһ��������������������Ĺ��ܣ�������������볤�Ⱥ�������ɵ����ݣ�
#  ������ɵ����ݿ����д�д��ĸ��A-Z����Сд��ĸ��a-z�������֣�0-9����������ţ�~!@#$%^&*()����
#  ����ֵΪ�����û�Ҫ�����ɵ��������


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

#2.�������Ϊһ�������б��һ���������жϸ������Ƿ�����ڸ��б��С�������ڣ������б�����߻����Ұ��

def judge2(number,lst):
	b=-1
	c=0
	d=[]
	for a in lst:
		if a==number:
			print("�б�����Ԫ��%d" %(number))
			c=1
			break
	if c==0:
		print("�б��ﲻ����Ԫ��%d" %(number))
	else:
            b = lst.index(number,b+1)
            d.append(b)
            for a in d:
	        if (len(lst) - 1) / 2 > a:
		    print("�����һ��")
		elif (len(lst)-1) / 2 < a:
	            print("�ұ���һ��")
		else:
		    print("�������м���һ��")

#3.����1-100�е�����

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

#4.��дһ��ģ�飬
#  Ҫ�������б���x��y���������add(x, y)���������sub(x, y)���������mul(x, y)���������div(x, y)���ĸ�������ʵ��

import demo
add(x,y)
sub(x,y)
mul(x,y)
def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('��������Ϊ0')

#5.���������һ�������б����ҳ����б�����С������������

def get_min_value(lst):
    from functools import reduce
    return reduce(lambda x, y: x if x < y else y, lst)

get_min_value([9,2,3,1,0,2,0.3,12])
          