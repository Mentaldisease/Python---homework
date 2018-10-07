课堂练习：

# 1、将字符串'hello, world'中的 l 替换为 *
‘hello,world’.replease('l','*')

# 2、现有字符串 'Good' ，期望结果 'good!good!good!'，至少用两种方法实现

(('Good{}'.lower()).format('!')) * 3

string = 'Good'.lower() + '!'
string + string + string

#3、将字符串 'Fh1qoWe92QbvC' 中的大写替换为小写，小写替换为大写（提示：Python 字符串有内置方法支持，请找到这个方法来实现）

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


# 4、请将字符串 'Fh1qoWe92QbvC' 中的数字按序取出，组成新的字符串并打印出来（提示：Python 字符串有内置方法可判断字符串是否为纯数字）
str = 'Fh1qoWe92QbvC'
num = ''.join([x for x in str if x.isdigit()])
print(num)

# 5、现有列表 lst = [2, 0, 3, 6, 9]，请打印出从小到大排列的列表 lst（不改变列表元素的原有顺序）
lst = [2, 0, 3, 6, 9]
sorted(lst)

# 6、现有一个列表 l = [2, 3, 1, 2, 4, 3]，请实现 l = [2, 3, 1, 4]
def unique_list(lst):
    seen = set()
    seen_add = seen.add
    return [x for x in lst if x not in seen and not seen_add(x)]

# 7、现有字符串 'aasdebbcaa'，请统计字符串中每个字符出现的次数，将统计结果存储在一个字典里
lst2 ='aasdebbcaa'
d = {}
for x in lst2:
    d[x] = lst2.count(x)

print(d)
  
# 8、完成一个函数，计算传入的字符串中的【数字】、【字母】、【空格】和【其他】的个数后返回
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

# 9、完成一个函数，检查传入的字符串是否含有空格，如果有空格则删去字符串中的空格并返回结果
def delspace(str):
    return ''.join([s for s in string if not s.isspace()])        

delspace(' a b c ')
# 10、完成一个函数：随机产生一个数，让用户来猜，猜中则屏幕打印"恭喜你猜对了"并结束，若猜错，则提示用户是猜大了还是猜小了（提示：内置的 random 模块有产生随机数的方法）
import random
def guess_number():
    true_num = random.randint(1, 100)
    user_num = int(input("请输入一个整数:"))
    count = 1
    while true_num != user_num:
        if true_num > user_num:
            print("太小了，请重新输入！")
        elif true_num < user_num:
            print("太大了，请重新输入！")
        count += 1
        user_num = int(input("请输入一个整数："))
    print("恭喜您，您猜对了！您一共猜了%d次" % count)

guess_number()