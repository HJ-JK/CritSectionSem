#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:44:30 2022

@author: hanjiezhu
"""
from multiprocessing import Process, BoundedSemaphore
from multiprocessing import current_process
from multiprocessing import Value

N = 8

def task(bs,common, tid):
    a = 0
    for i in range(100):
        print(f'{tid}−{i}: Non−critical Section')
        a += 1
        print(f'{tid}−{i}: End of non−critical Section')
        
        bs.acquire()
        try:
            print(f'{tid}−{i}: Critical section')
            v = common.value + 1
            print(f'{tid}−{i}: Inside critical section')
            common.value = v
            print(f'{tid}−{i}: End of critical section')
        finally:
            bs.release()
        
def main():
    lp = []
    common = Value('i', 0)
    bd = BoundedSemaphore(1)
    for tid in range(N):
        lp.append(Process(target=task, args=(bd, common, tid)))
    print (f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start()
    for p in lp:
        p.join()
    print (f"Valor final del contador {common.value}")
    print ("fin")
if __name__ == "__main__":
    main()
