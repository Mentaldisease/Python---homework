������ϰ��

# 1�����ַ���'hello, world'�е� l �滻Ϊ *
��hello,world��.replease('l','*')

# 2�������ַ��� 'Good' ��������� 'good!good!good!'�����������ַ���ʵ��

(('Good{}'.lower()).format('!')) * 3

string = 'Good'.lower() + '!'
string + string + string

#3�����ַ��� 'Fh1qoWe92QbvC' �еĴ�д�滻ΪСд��Сд�滻Ϊ��д����ʾ��Python �ַ��������÷���֧�֣����ҵ����������ʵ�֣�

'FhIqoWe92QbvC'.swapcase()

def swape(lst):
    str = []
    for x in lst:
        if x.isalpha():
            if x.islower():
                x = x.upper()
            else:
                x = x.lower()
        str.append(x)
    return ''.join(str)


# 4���뽫�ַ��� 'Fh1qoWe92QbvC' �е����ְ���ȡ��������µ��ַ�������ӡ��������ʾ��Python �ַ��������÷������ж��ַ����Ƿ�Ϊ�����֣�
str = 'Fh1qoWe92QbvC'
num = ''.join([x for x in str if x.isdigit()])
print(num)

# 5�������б� lst = [2, 0, 3, 6, 9]�����ӡ����С�������е��б� lst�����ı��б�Ԫ�ص�ԭ��˳��
lst = [2, 0, 3, 6, 9]
sorted(lst)

# 6������һ���б� l = [2, 3, 1, 2, 4, 3]����ʵ�� l = [2, 3, 1, 4]
def unique_list(lst):
    seen = set()
    seen_add = seen.add
    return [x for x in lst if x not in seen and not seen_add(x)]

# 7�������ַ��� 'aasdebbcaa'����ͳ���ַ�����ÿ���ַ����ֵĴ�������ͳ�ƽ���洢��һ���ֵ���
lst2 ='aasdebbcaa'
d = {}
for x in lst2:
    d[x] = lst2.count(x)

print(d)
  
# 8�����һ�����������㴫����ַ����еġ����֡�������ĸ�������ո񡿺͡��������ĸ����󷵻�
counter = {'number': 0, 'letter': 0, 'space': 0, 'others': 0}
others = 0
def count1(str):
    for n in list(str):
        if x.isdigit:
            counter['number'] += 1
        elif x.isalpha:
            counter['letter'] += 1
        elif x.isspace:
            counter['space'] += 1
        else:
            counter['others'] += 1
    return counter

print(str_counter('hello world 2333#!:|'))

# 9�����һ����������鴫����ַ����Ƿ��пո�����пո���ɾȥ�ַ����еĿո񲢷��ؽ��
def delspace(str):
    return ''.join([s for s in string if not s.isspace()])        

delspace(' a b c ')
# 10�����һ���������������һ���������û����£���������Ļ��ӡ"��ϲ��¶���"�����������´�����ʾ�û��ǲ´��˻��ǲ�С�ˣ���ʾ�����õ� random ģ���в���������ķ�����
import random
def guess_number():
    true_num = random.randint(1, 100)
    user_num = int(input("������һ������:"))
    count = 1
    while true_num != user_num:
        if true_num > user_num:
            print("̫С�ˣ����������룡")
        elif true_num < user_num:
            print("̫���ˣ����������룡")
        count += 1
        user_num = int(input("������һ��������"))
    print("��ϲ�������¶��ˣ���һ������%d��" % count)

guess_number()