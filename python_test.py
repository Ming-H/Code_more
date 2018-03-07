1、对list去重
l1 = [1,1,2,3,2]
print(list(set(l1)))

l2 = {}.fromkeys(l1).keys()
print(l2)

l1 = ['b','c','d','b','c','a','a']
l2 = []
[l2.append(item) for item in l1 if not item in l2]

2、创建字典
dict1 = {}.fromkeys(('x','y'),-1)
print(dict1)
dict2 = {}.fromkeys(('a','b','c'))
print(dict2)

3、合并两个有序list
#遍历两个list，选择小的加入到新list
def func(L1,L2):
    L = []
    while len(L1)>0 and len(L2)>0:
        if L1[0] < L2[0]:
            L.append(L1[0])
            del L1[0]
        else:
            L.append(L2[0])
            del L2[0]
    L.extend(L1)
    L.extend(L2)
    print(L)
    
#******pop方法******
def func(L1,L2):
    L= []
    while L1 and L2:
        if L1[0] >= L2[0]:
            L.append(L2.pop(0))
        else:
            L.append(L1.pop(0))
    while L1:
        L.append(L1.pop(0))
    while L2:
        L.append(L2.pop(0))
    print(L)
    
#******尾递归方法*******
def _recursion_merge_sort2(l1, l2, tmp):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return _recursion_merge_sort2(l1, l2, tmp)
    
def recursion_merge_sort2(l1, l2):
    result = _recursion_merge_sort2(l1, l2, [])
    return result

4、交叉链表求交点
#******如果两个链表交叉，则从交叉点开始，后面的元素均相同******
a = [1,2,3,7,8,9,1,5]
b = [4,5,7,9,1,5]
for i in range(1,min(len(a),len(b))):
    if i==1 and (a[-1] != b[-1]):
        print("No")
        break
    else:
        if a[-i] != b[-i]:
            print("交叉节点：",a[-i+1])
            break
        else:
            pass
        
5、字典排序
d = {'a':5, 'b':4, 'e':83, 'z':42, 'h':33}
#根据key排序
d_sort_key = sorted(d.items(), key=lambda k: k[0])  
[(k,d[k]) for k in sorted(d.keys())] 
#根据value排序
d_sort_value = sorted(d.items(), key = lambda k: k[1]) 
#通过公共键对字典列表进行排序
l = [{'x':1, 'y':2}, {'x':2, 'y':3}, {'x':3, 'y':4}]
L_new = sorted(l, key=lambda k: k['x'], reverse = True)

6、替换字符串指定字符
#subn()方法执行的效果跟sub()一样，不过它会返回一个二维数组，包括替换后的新的字符串和总共替换的数量
import re
p = re.compile('blue|white|red')
print(p.subn('color','blue socks and red shoes'))
>>('color socks and color shoes', 2)

7、match()和search()的区别
re模块中match(pattern,string[,flags]),是从字符串首字母处匹配
re模块中research(pattern,string[,flags]),是遍历整个字符串匹配
import re
print(re.match('super', 'superstition').span())
>>(0, 5)
print(re.search('super', 'insuperable').span())
>>(2, 7)

8、正则表达式里<.*>和<.*?>的区别
( <.*> )  贪婪匹配
(<.*?> )  非贪婪匹配

9、函数传值还是传引用
说传值或者传引用都不准确，非要安一个确切的叫法的话，叫传对象
错误：
def bad_append(new_item, a_list=[]):
    a_list.append(new_item)
    return a_list

正确：
def good_append(new_item, a_list=None):
    if a_list is None:
        a_list = []
    a_list.append(new_item)
    return a_list

10、函数参数类型
必选参数、默认参数、可选参数、关键字参数
def func(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

11、浮点数比较
浮点数相等比较不能通过==,应该是一个范围,可以使用 x <= 1.0
x = 0.5
while x != 1.0
    print(x)
    x += 0.1
>>SyntaxError: invalid syntax

12、copy.copy和copy.deepcopy的区别 
import copy
lista = [1,2,3,['a','b']]
listb = copy.copy(lista)
listc = copy.deepcopy(lista)

lista.append(5)
lista[3].append('c')

print(lista)
[1, 2, 3, ['a', 'b', 'c'], 5]
print(listb)
[1, 2, 3, ['a', 'b', 'c']]
print(listc)
[1, 2, 3, ['a', 'b']]

13、什么是装饰器，如何使用装饰器
def log(level):
    def dec(func):
        def wrapper(*kargc,**kwargs):
            print("before func was called")
            func(*kargc,**kwargs)
            print("after func was called")
        return wrapper
    return dec

@log(2)
def funcLog():
    print("funcLog was called")
    
funcLog()

>>before func was called
>>funcLog was called
>>after func was called

14、交换字典的键和值
d = {'A' : 1, 'B' : 2, 'C' : 3}
(1) 字典推导式
d1 = {v:k for k,v in d.items()}
生成器表达式 + dict()
(2) d2 = dict((v,k) for k,v in d.items())
zip() + dict()
(3) d3 = dict(zip(d.values(), d.keys()))

15、求斐波那契数列的第n项
def Fibonacci(n):
    prev, curr = 0, 1
    for _ in range(n):
        prev, curr = curr, prev+curr
    return prev


参考文献：
https://github.com/taizilongxu/interview_python#29-super-init
http://www.cnblogs.com/ChenxofHit/archive/2011/03/18/1988431.html
https://www.cnblogs.com/shizhengwen/p/6972183.html
http://blog.csdn.net/u013679490/article/details/54948759
http://www.codingonway.com/python-get-fibonacci-n-number.html
