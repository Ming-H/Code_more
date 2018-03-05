#-*- coding:utf-8 -*-
"""
对给定序列号段，产生相应校验位，将最终序列号输出到txt文件

计算步骤如下：

　　步骤1：从右边第1个数字（低序）开始每隔一位乘以2。
　　步骤2：把在步骤1中获得的乘积的各位数字与原号码中未乘2的各位数字相加。
　　步骤3：从邻近的较高的一个以0结尾的数中减去步骤2中所得到的总和［这相当于求这个总和的低位数字（个位数）的“10的补数”］。
          如果在步骤2得到的总和是以零结尾的数（如30、40等等），则校验数字就是零。
　　例：
　　　　无校验数字的卡号　4992　73　9871　步骤
　　4　9 　9　2　7　3　9　8　7　1　　　　　　　1
　　　×2　 ×2 　×2 　×2　 ×2 
　　　18　　　4　　 6　　16　　2

　　4+1+8+9+4+7+6+9+1+6+7+2=64　　　　　　　　 2
　　70-64=6　　　　　　　　　　　　　　　　　　3

　　带有校验数字的卡号为：4992　73　9871　6
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
