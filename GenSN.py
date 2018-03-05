#-*- coding:utf-8 -*-
"""
对给定序列号段，产生相应校验位，将最终序列号输出到txt文件
"""

## 产生初始序列号段，不带校验位
def func_OrignNum(start, end):
    name = "SN_"+str(start)
    with open(name+'.txt','w') as file:
        for i in range(start, end+1):
            file.write(str(i)+'\n')
    return name

## 产生校验位
def func_CheckNum(SN):
    TestString = [2,1,2,1,2,1,2,1,2]  # 490000139
    sum_each = 0
    sum = 0
    for i in range(len(SN)):
        sum_each = TestString[i] * SN[i]
        while sum_each >= 10:
            sum_each = sum_each % 10 + sum_each // 10
        sum += sum_each
    CheckNum = 10 - (sum % 10)
    if CheckNum==10:
        CheckNum = 0
    return CheckNum
    
    
## 添加校验位
def func_AddCheck(SN_file):
    new_sn = []
    with open(SN_file) as file:
        lines = file.readlines()
        for line in lines:
            line_new = [int(item) for item in line.strip()]
            CheckNum = func_CheckNum(line_new)
            line_new.append(CheckNum)   
            new_sn.append(line_new)
    with open("New"+SN_file,'w') as file:
        for item in new_sn:
            for num in item:
                file.write(str(num))
            file.write('\n')
            
            
if __name__ == "__main__":
    name = func_OrignNum(481165301, 481166300)
    func_AddCheck(name+'.txt')
