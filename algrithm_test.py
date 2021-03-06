1、在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

def is_in(l,num):
    m = len(l)-1
    n = 0
    while n<len(l) and m>=0:
        if l[m][n] > num:
            m -= 1
        if l[m][n] < num:
            n += 1
        if l[m][n] == num:
            print(l[m][n])
            print("ok")
            break
    return Flase

if __name__ == "__main__":
    l = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(l)
    is_in(l,9)
    
 
2、找零问题
这是一个典型的动态规划问题，我们可以从1开始记录下每个钱数所需的硬币枚数，避免重复计算，为了能够输出硬币序列，我们还需要记录下每次新加入的硬币。
下面给出用动态规划解决此问题的递推式：
参数说明： 当只用面值为T[1],T[2],…T[n]来找出钱j时，所用的硬币的最小个数记为C(i,j),则C(i,j)的递推方程为： C(i,j) = min(C(i-1,j)+1)
def  coinChange( values,valuesCounts,  money, coinsUsed): 
    #values    T[1:n]数组
    #valuesCounts   钱币对应的种类数
    #money  找出来的总钱数
    #coinsUsed   对应于目前钱币总数i所使用的硬币数目
    for cents in range(1, money+1):
        minCoins = cents     #从第一个开始到money的所有情况初始
        for kind in range(0, valuesCounts):
            if(values[kind] <=cents):
                temp = coinsUsed[cents - values[kind]] +1
                if(temp < minCoins):
                    minCoins = temp 
        coinsUsed[cents] = minCoins
        print('面值为：{0} 的最小硬币数目为：{1} '.format(cents, coinsUsed[cents]) )
 
if '__name__ = __main__':
    values = [ 25, 21, 10, 5, 1]
    money = 63
    coinsUsed= [0]*(money+1)
    len  = len(values)
    coinChange(values, len, money, coinsUsed)
    
    
3、两个字符串是否是变位词
class Anagram:
    """
    @:param s1: The first string
    @:param s2: The second string
    @:return true or false
    """
    def Solution1(s1,s2):
        alist = list(s2)
        pos1 = 0
        stillOK = True
        while pos1 < len(s1) and stillOK:
            pos2 = 0
            found = False
            while pos2 < len(alist) and not found:
                if s1[pos1] == alist[pos2]:
                    found = True
                else:
                    pos2 = pos2 + 1
            if found:
                alist[pos2] = None
            else:
                stillOK = False
            pos1 = pos1 + 1
        return stillOK
    print(Solution1('abcd','dcba'))

    #对两个字符串进行排序，如果是变位词，则排序后的结果应该相同，时间复杂度为O(lgN)
    def Solution2(s1,s2):
        alist1 = list(s1)
        alist2 = list(s2)
        alist1.sort()
        alist2.sort()
        pos = 0
        matches = True
        while pos < len(s1) and matches:
            if alist1[pos] == alist2[pos]:
                pos = pos + 1
            else:
                matches = False
        return matches
    print(Solution2('abcde','edcbg'))

    #将字符转化为数字，然后遍历每一个字符串，得到对应的数组，判断两个数组是否相等，时间复杂度为O(N)
    def Solution3(s1,s2):
        c1 = [0]*26
        c2 = [0]*26
        for i in range(len(s1)):
            pos = ord(s1[i])-ord('a')
            c1[pos] = c1[pos] + 1
        for i in range(len(s2)):
            pos = ord(s2[i])-ord('a')
            c2[pos] = c2[pos] + 1
        j = 0
        stillOK = True
        while j<26 and stillOK:
            if c1[j] == c2[j]:
                j = j + 1
            else:
                stillOK = False
        return stillOK
    print(Solution3('apple','pleap'))

    
4、最大多位数
设有n个正整数，将他们连接成一排，组成一个最大的多位整数。
如:n=3时，3个整数13,312,343,连成的最大整数为34331213。
如:n=4时,4个整数7,13,4,246连接成的最大整数为7424613。
输入描述:
有多组测试样例，每组测试样例包含两行，第一行为一个整数N（N<=100），第二行包含N个数(每个数不超过1000，空格分开)。
输出描述:
每组数据输出一个表示最大的整数。
(1)
n = raw_input()
x = raw_input().split(' ')
x.sort(cmp=lambda x,y:cmp(x+y, y+x), reverse=True)
print "".join(x)
(2)
def func():
    n = int(input())
    num_list = input().split()
    if len(num_list) != n:
        return False
    else:
        sorted_list = []
        while num_list:
            cur_num = num_list[0]
            for item in num_list:
                if cur_num + item < item + cur_num:
                    cur_num = item
            sorted_list.append(cur_num)
            num_list.remove(cur_num)
        return sorted_list
    
if __name__ == "__main__":
    func()

5、句子反转
给定一个句子（只包含字母和空格）， 将句子中的单词位置反转，单词用空格分割, 单词之间只有一个空格，前后没有空格。 
比如： （1） “hello xiao mi”-> “mi xiao hello”
输入描述:
输入数据有多组，每组占一行，包含一个句子(句子长度小于1000个字符)
输出描述:
对于每个测试示例，要求输出句子中单词反转后形成的句子

def func():
    L = input().split()
    print(L)
    print(" ".join(L[::-1]))
    
if __name__ == "__main__":
    func()

6、电话号码分身
继MIUI8推出手机分身功能之后，MIUI9计划推出一个电话号码分身的功能：首先将电话号码中的每个数字加上8取个位，然后使用对应的大写字母代替 （"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"）， 然后随机打乱这些字母，所生成的字符串即为电话号码对应的分身。
输入描述:
第一行是一个整数T（1 ≤ T ≤ 100)表示测试样例数；接下来T行，每行给定一个分身后的电话号码的分身（长度在3到10000之间）。
输出描述:
输出T行，分别对应输入中每行字符串对应的分身前的最小电话号码（允许前导0）。
示例1
输入
4
EIGHT
ZEROTWOONE
OHWETENRTEO
OHEWTIEGTHENRTEO
输出
0
234
345
0345

import sys
def originalDigits(s):
    result = [0]*10
    result[0] = s.count("Z")
    result[2] = s.count("W")
    result[4] = s.count("U")
    result[6] = s.count("X")
    result[7] = s.count("S") - result[6]
    result[5] = s.count("V") - result[7]
    result[1] = s.count("O") - result[0] - result[4] - result[2]
    result[9] = (s.count("N") - result[1] - result[7]) // 2
    result[8] = s.count("I") - result[5] - result[6] - result[9]
    result[3] = s.count("H") - result[8]

    t, resStr = "", ""
    for i, r in enumerate(result):
        t += r * str(i)
    
    for i in t:
        if int(i) >= 8:
            resStr += str(int(i) - 8)
        else:
            resStr += str(int(i) + 10 - 8)
    return "".join(sorted(resStr))  
    
if __name__ == "__main__":
    ss = "OHEWTIEGTHENRTEO"
    print(originalDigits(ss.strip()))

6、水仙花数
春天是鲜花的季节，水仙花就是其中最迷人的代表，数学上有个水仙花数，他是这样定义的： “水仙花数”是指一个三位数，
它的各位数字的立方和等于其本身，比如：153=1^3+5^3+3^3。 现在要求输出所有在m和n范围内的水仙花数。
输入描述:
输入数据有多组，每组占一行，包括两个整数m和n（100 ≤ m ≤ n ≤ 999）。
输出描述:
对于每个测试实例，要求输出所有在给定范围内的水仙花数，就是说，输出的水仙花数必须大于等于m,并且小于等于n，
如果有多个，则要求从小到大排列在一行内输出，之间用一个空格隔开; 如果给定的范围内不存在水仙花数，则输出no;
每个测试实例的输出占一行。
示例1
输入
100 120
300 380
输出
no
370 371

def func():
    m, n = map(int, input().split())
    num_list = []
    for item in range(m, n+1):
        if item == sum(int(x)**3 for x in str(item)):
            num_list.append(item)
    if len(num_list) == 0:
        print("no")
    else:
        print(" ".join(map(str, num_list)))

        n, m = map(int, input().split())

7、求数列的和
数列的第一项为n，以后各项为前一项的平方根，求数列的前m项的和。
输入描述:
输入数据有多组，每组占一行，由两个整数n（n < 10000）和m(m < 1000)组成，n和m的含义如前所述。
输出描述:
对于每组输入数据，输出该数列的和，每个测试实例占一行，要求精度保留2位小数。
示例1
输入
81 4
2 2
def func():
    sum = 0
    for i in range(m):
        sum += n
        n = n**0.5
    print('%.2f' % sum)

8、袋鼠过河
一只袋鼠要从河这边跳到河对岸，河很宽，但是河中间打了很多桩子，每隔一米就有一个，每个桩子上都有一个弹簧，
袋鼠跳到弹簧上就可以跳的更远。每个弹簧力量不同，用一个数字代表它的力量，如果弹簧力量为5，就代表袋鼠下一跳最多能够跳5米，
如果为0，就会陷进去无法继续跳跃。河流一共N米宽，袋鼠初始位置就在第一个弹簧上面，要跳到最后一个弹簧之后就算过河了，
给定每个弹簧的力量，求袋鼠最少需要多少跳能够到达对岸。如果无法到达输出-1
输入描述:
输入分两行，第一行是数组长度N (1 ≤ N ≤ 10000)，第二行是每一项的值，用空格分隔。
输出描述:
输出最少的跳数，无法到达输出-1
示例1
输入
5
2 0 1 1 1
输出
4
def func():
    N = int(input())
    L = list(map(int, input().split()))
    sum = L[0]
    left = 0  
    right = L[0]
    count = 1
    while sum < N:  
        max_num = max(L[left + 1 : right+1])
        if max_num == 0:
            break
        left = L.index(max_num)
        right = left + max_num
        sum += max_num
        count += 1
    if count == 1:
        print(-1)
    else:
        print(count)
        
9、彩色宝石项链
有一条彩色宝石项链，是由很多种不同的宝石组成的，包括红宝石，蓝宝石，钻石，翡翠，珍珠等。有一天国王把项链赏赐给了一个学者，
并跟他说，你可以带走这条项链，但是王后很喜欢红宝石，蓝宝石，紫水晶，翡翠和钻石这五种，我要你从项链中截取连续的一小段还给我，
这一段中必须包含所有的这五种宝石，剩下的部分你可以带走。如果无法找到则一个也无法带走。请帮助学者找出如何切分项链才能够拿到最多的宝石。
输入描述:
我们用每种字符代表一种宝石，A表示红宝石，B表示蓝宝石，C代表紫水晶，D代表翡翠，E代表钻石，F代表玉石，G代表玻璃等等，
我们用一个全部为大写字母的字符序列表示项链的宝石序列，注意项链是首尾相接的。每行代表一种情况。
输出描述:
输出学者能够拿到的最多的宝石数量。每行一个
示例1
输入
ABCYDYE
ATTMBQECPD
输出
1
3
def func():
    try:
        L = input()
        n = len(L)
        min = n
        for i in range(n):
            tmp = []
            for j in 'ABCDE':
                tmp.append(L.find(j))
            tmp.sort()
            if min > tmp[-1]:
                min = tmp[-1]
            L = L[1:] + L[0]
        print(L-min-1)
    except:
        break
        
 10、统计字符
给定一个英文字符串,请写一段代码找出这个字符串中首先出现三次的那个英文字符。
输入描述:
输入数据一个字符串，包括字母,数字等。
输出描述:
输出首先出现三次的那个英文字符
示例1
输入
Have you ever gone shopping and
输出
e
def func():
    num = input()
    d = {}
    for item in num:
        if item.isalpha() is True:
            if item not in d:
                d[item] = 1
            else:
                d[item] += 1
                if d[item] >=3:
                    print(item)
                    break















参考文献：
https://github.com/taizilongxu/interview_python#29-super-init
http://www.cnblogs.com/ChenxofHit/archive/2011/03/18/1988431.html
https://www.nowcoder.com/questionTerminal/493d71a992f44554a500ed818056e1a6



    
