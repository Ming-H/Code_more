# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 15:09:39 2018

@author: HM
"""

import time, threading

def loop():
    print("thread %s is running..." % threading.current_thread().name)
    n = 0
    while n<5:
        n += 1
        print("thread %s >>> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("thread %s ended." % threading.current_thread().name)
    
    
def my_loop1():
    print("thread %s is running..." % threading.current_thread().name)
    print("thread %s ended." % threading.current_thread().name)
    
def my_loop2():
    print("thread %s is running..." % threading.current_thread().name)
    print("thread %s ended." % threading.current_thread().name)
    
def my_loop3():
    print("thread %s is running..." % threading.current_thread().name)
    print("thread %s ended." % threading.current_thread().name)
    
def my_loop4():
    print("thread %s is running..." % threading.current_thread().name)
    print("thread %s ended." % threading.current_thread().name)
    
def my_loop5():
    print("thread %s is running..." % threading.current_thread().name)
    print("thread %s ended." % threading.current_thread().name)
    
def my_loop6():
    print("thread %s is running..." % threading.current_thread().name)
    print("thread %s ended." % threading.current_thread().name)
    
def my_loop7():
    print("thread %s is running..." % threading.current_thread().name)
    print("thread %s ended." % threading.current_thread().name)
    

if __name__ == "__main__":
    print("thread %s is running..." % threading.current_thread().name)
    t = threading.Thread(target=loop)
    g1 = threading.Thread(target=my_loop1)
    g2 = threading.Thread(target=my_loop2)
    g3 = threading.Thread(target=my_loop3)
    g4 = threading.Thread(target=my_loop4)
    g5 = threading.Thread(target=my_loop5)
    g6 = threading.Thread(target=my_loop6)
    g7 = threading.Thread(target=my_loop7)
    t.start()
    g1.start()
    g2.start()
    g3.start()
    g4.start()
    g5.start()
    g6.start()
    g7.start()
    
    t.join()
    g1.join()
    g2.join()
    g3.join()
    g4.join()
    g5.join()
    g6.join()
    g7.join()
    
    print("thread %s ended." % threading.current_thread().name)
    
#线程之间共享变量时，当一个线程对变量进行改变时，应该加锁来保证一个线程执行时，
#其他线程无法对该变量进行运算
balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
    
def run_thread(n):
    for i in range(1000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
            
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance) 
 
"""
因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的
线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能
交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立
的GIL锁，互不影响。
"""

参考文献：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000
    
    
