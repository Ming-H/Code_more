
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

if __name__ == "__main__":
    l = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(l)
    is_in(l,9)
    
    
2、
    
