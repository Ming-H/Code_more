# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 14:19:55 2018

@author: HM

WangJK 数据处理并画图
通过最小二乘法拟合曲线，求出函数中的四个参数
"""
import pandas as pd
import numpy as np
from scipy.optimize import leastsq
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

###需要拟合的函数func及误差error###
def func_small(x,a1,a2):
    return (x**2-a1)**2 + a2*(x**2)

def func(f, fr0, fr1, r0, r1):
    A = fr0**2
    B = fr1**2
    C = (r0/(2*np.pi))**2
    D = (r1/(2*np.pi))**2
    H1 = B * np.sqrt(func_small(f, A, C))              
    H2 = A * np.sqrt(func_small(f, B, D))
    H = 10 * np.log10(H1/H2)
    return H

def func_error (p, f, h):
    fr0, fr1, r0, r1 = p
    return func(f, fr0, fr1, r0, r1) - h


if __name__ == "__main__":
    data = pd.read_csv("F:/CodeMore/data.csv")
    
    #原始数据三分之二，每隔5个取一个点
    #f = np.array(data['f'][0:280:5])
    #h = np.array(data['h_new'][0:280:5])
    
     #平滑数据三分之二，每隔5个取一个点
    f = np.array(data['f'][0:267:5])
    h_list = ['h1', 'h2', 'h3', 'h4']
    for item in h_list:
        h = np.array(data[item][0:267:5])
        p0 = [6.0e+9, 8.0e+9, 18.0e+9, 24.0e+9]
        #print(func_error(p0, f[0], h[0]))
        
        plesq = leastsq(func_error, p0, args=(f, h))
        fr0, fr1, r0, r1 = plesq[0]
        print("fr0=",fr0,'\n', "fr1=",fr1, '\n', "r0=", r0, '\n', "r1=",r1)
        
        ###绘图，看拟合效果###
        plt.figure(figsize=(8,6))
        plt.plot(f, h, '*',label='Sample Point')
        #plt.scatter(f,h,color="red",label="Sample Point",linewidth=3) #画样本点
        y= func(f, fr0, fr1, r0, r1)
        plt.plot(f,y,color="red",label="Fitting Line",linewidth=2) #画拟合直线
        plt.legend()
        name = item + str(plesq[0]) 
        plt.title(name)  
        plt.savefig('F:/CodeMore/'+name+'.png')
        plt.show()
    
