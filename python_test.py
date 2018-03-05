
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
    
    
2、对list去重
l1 = [1,1,2,3,2]
print(list(set(l1)))

l2 = {}.fromkeys(l1).keys()
print(l2)

l1 = ['b','c','d','b','c','a','a']
l2 = []
[l2.append(item) for item in l1 if not item in l2]

3、创建字典
dict1 = {}.fromkeys(('x','y'),-1)
print(dict1)
dict2 = {}.fromkeys(('a','b','c'))
print(dict2)

4、合并两个有序list
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

5、交叉链表求交点
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
        
6、二分查找
def func(L, item):
    i = 0
    j = len(L)-1
    while i<=j:
        mid = int((i+j)/2)
        guess = L[mid]
        if guess>item:
            j = mid - 1
        elif guess < item:
            i = mid + 1
        else:
            return mid
    return False

7、快速排序
def func(L):
    if len(L)<2:
        return L
    else:
        pivot = L[-1]
        less = [item for item in L[:-1] if item <= pivot]
        bigger = [item for item in L[:-1] if item > pivot]
        final = func(less) + [pivot] + func(bigger)
        return final

#部分内容来源于https://github.com/taizilongxu/interview_python#29-super-init
