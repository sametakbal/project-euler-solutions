# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 23:00:36 2019

@author: samet
"""

def check_prime(num):
    i=2
    while(i<=(num**(0.5))):
        if num % i == 0:
            return False
        i+=1
    return True
total=5  # 2,3
i=1
while((i*6+1)<2000000):
    if check_prime(i*6+1):
        total+=(i*6+1)
    if check_prime(i*6-1):
        total+=(i*6-1)
    i+=1
print(total)