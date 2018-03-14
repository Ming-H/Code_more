# -*- coding: utf-8 -*-
# Created on Wed Mar 14 09:42:08 2018
# @author: HM

"""
查找（Searching）就是根据给定的某个值，在查找表中确定一个其关键字等于给定值的数据元素（或记录）。
"""

# 无序查找，数据不排序的线性查找，遍历数据元素， 时间复杂度O(n)
def sequential_search(L, target):
    for i in range(len(L)):
        if L[i] == target:
            return i
    else:
         return False
     
# 二分查找，查找表中的数据必须按某个主键进行某种排序，时间复杂度为O(log(n))
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
        
