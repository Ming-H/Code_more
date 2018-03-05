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



参考文献：
https://github.com/taizilongxu/interview_python#29-super-init
http://www.cnblogs.com/ChenxofHit/archive/2011/03/18/1988431.html



    
