# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 09:42:08 2018

@author: HM
"""
#无序查找， 时间复杂度O(n)
def sequential_search(L, target):
    for i in range(len(L)):
        if L[i] == target:
            return i
    else:
         return False
     
#二分查找，时间复杂度为O(log(n))
def binary_search(L, target):
    i = 0
    j = len(L) - 1
    while i<=j:
        mid = (i+j)/2
        guess = L[mid]
        if guess>target:
            j = mid - 1
        elif guess<target:
            i = mid + 1
        else:
            return mid
    return False

# 插值排序 以更快的速度进行缩减 时间复杂度O(log(n))
# 插值的核心就是使用公式： value = (target - list[low])/(list[high] - list[low])
# 其优点是，对于表内数据量较大，且关键字分布比较均匀的查找表，使用插值算法的平均性能比二分查找要好得多。
# 反之，对于分布极端不均匀的数据，则不适合使用插值算法。
def insert_sort(L, target):
    i = 0
    j = len(L) - 1
    while(i<=j):
        mid = i + int((j-i)*(target-L[i])/(L[j]-L[i]))
        guess = L[mid]
        if target < guess:
            j = mid - 1
        elif target > guess:
            i = mid + 1
        else:
            return mid
    return False
      
    
#最大子列和问题
def max_sum(L):
    max = 0
    current = 0
    for item in L:
        current += item
        if current > max:
            max = current
        if current < 0:
            current = 0
    return max

if __name__ == "__main__":
    L = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    item = 22
    result = insert_sort(L, item)
    print(result)
