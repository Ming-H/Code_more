#冒泡排序
"""
冒泡排序的思想: 每次比较两个相邻的元素, 如果他们的顺序错误就把他们交换位置
冒泡排序原理: 每一趟只能将一个数归位, 如果有n个数进行排序,只需将n-1个数归位, 
也就是说要进行n-1趟操作(已经归位的数不用再比较)
"""
def bubble_sort(L):
    for i in range(len(L)-1):
        for j in range(len(L)-1-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[i]
    return L
    
#插入排序
"""
将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，
算法适用于少量数据的排序
"""
def insert_sort(L):
    for i in range(1, len(L)):
        tmp = L[i]
        j = i-1
        while j>=0 and L[j]>tmp:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = tmp
    return L

def insert_sort(L):
    for i in range(1, len(L)):
        tmp = L[i]
        j = i-1
        while j>=0:
            if L[j]>tmp:
                L[j+1] = L[j]
                L[j] = tmp
            j -= 1
    return L 
    
#快速排序
"""
将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，
算法适用于少量数据的排序
"""   
def quick_sort(myList, start, end):
    if start < end:
        i,j = start,end
        base = myList[i]
        while i < j:
            while (i < j) and (myList[j] >= base):
                j = j - 1
            myList[i] = myList[j]
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        myList[i] = base    #important, not (base = myList[j])
        quick_sort(myList, start, i - 1)
        quick_sort(myList, j + 1, end)
    return myList
      
nums = [9999,5,2,45,6,8,2,1]
print(quick_sort(nums, 0, len(nums)-1))
      
          
#归并排序
"""
首先归并排序使用了二分法，归根到底的思想还是分而治之。拿到一个长数组，将其不停的分为左边和右边两份，
然后以此递归分下去。然后再将她们按照两个有序数组的样子合并起来。
"""                 
def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1
    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)/2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)

if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9]
    print merge_sort(a)
       
 参考文献：https://www.cnblogs.com/piperck/p/6030122.html           
