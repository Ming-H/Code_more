# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 15:09:39 2018

@author: HM
"""

with open('file.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())
        
       
#字符编码
#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，
#例如，读取GBK编码的文件
f = open("file.txt", 'r', encoding='gbk')
f.read()

f = open('gbk.txt', 'r', encoding='gbk', errors='ignores')

from io import StringIO
f = StringIO()
f.write('Hello')

from io import StringIO
f = StringIO('Hello')
while True:
    s = f.readline()
    if s=='':
        break
    print(s.strip())
    
    
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()

import os
os.name
os.uname()
os.environ
os.environ.get('PATH')
os.path.abspath('.')
os.path.join('/user/', 'testdir')

os.mkdir('/user/test')
os.rmdir('/user/test')
os.path.split('?user/file.txt')
os.path.splitext('/path/file.txt')

os.rename('test.txt','test.py')

[x for x in os.listdir('.') if os.path.isdir(x))]
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

[x for x in os.listdir('.') if os.path.isfile(x) and os.path.solitext(x)[1]=='.py']


for x in os.listdir(p):
    p1 = os.path.join(os.path.abspath(p),x)
    if w in x:
        print(p1)
    if os.path.isdir(p1):
        findStr(p1, w)
        

        
        


