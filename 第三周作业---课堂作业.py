#1.��ȡ�û���������֣�name�������䣨age��������һ�¸��û�����һ��Ϊ100��

def years():
    name = input("name:")
    age = int(input("age:"))
    years = 100 + 2018 - age
    print(f'{name} �� {years} ��Ϊ 100 ��')


years()

#2.��ȡ�û��������������������������ӡ������������������������ż�����ӡ�����������ż����

def judge():
    number = int(input("����һ������:"))
    if number % 2 == 0:
        print("���������ż��")
    elif number % 2 == 1:
        print("�������������")
    else:
        print("���������0")

judge()

#3.���������һ�� list���жϸ� list ���Ƿ��пն������������ַ���ʵ�֣�
#һ��
def judgelist(list):
    print(all(list))

judgelist([0,''])
#����
def judgelist(lst):
    return list(filter(None, lst)) == lst

judgelist([])
#����
def judgelist(list):
    if 0 == len(list):
        print('list is false')
    else:
        print('list is ture')

judgelist([])

#4.���������һ�������б��Ѹ��б���ÿ��������ƽ���󷵻��µ��б����������ַ���ʵ�֣�

#һ��
lst = [1,2,3,4]
def judgeint(lst):
    lst2 = [x * 2 for x in lst]
    print(lst2)

judgeint(lst)

#����
lst = [1,2,3,4]
def judgeint(lst):
    lst2 = map(lambad x : �� * 2,lst)
    print(list(lst2))

judgeint(lst)


#5.���������һ�������б�ʹ�� reduce ����ʵ����ͺ󷵻ؽ��

lst = [1,2,3,4]
def list2(lst):
    from functools import reduce
    return (reduce(lambda x,y : x + y,lst)

list2(lst)

#6.�����б��Ƶ�ʽʵ������
lst = [1,2,3,4]
def list3(lst):
    lst2 = [x **3 for x in lst]
    print(lst2)

list3(lst)

#7.������������� list���뷵�����ǵĹ�ͬԪ������ɵ����б�
lst1 = [1,2,4]
lst2 = [3,6,8]
def list4(lst1 , lst2):
    s = set(m) & set(n)
    return list(s)

list4(lst1,lst2)

#8.�ҳ����������е�����������������ַ���ʵ�֣�

#һ��
def max3():
    from functools import reduce
    return reduce(lambda x, y: x if x > y else y, (x, y, z))

max3()

#����
import math
def max3(x,y,z):
    return print(max(x,y,z))

max(1,9,2)