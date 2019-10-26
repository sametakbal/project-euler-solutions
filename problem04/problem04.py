# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 21:49:03 2019

@author: samet
"""
def check_palindrome(num):
    n = len(num)-1
    for i in range(0,n):
        if(num[i]!=num[n-i]):
            return False
    return True
max=0
for i in range(999,100,-1):
    for j in range(999,100,-1):
        if((i*j)>max and check_palindrome(str(i*j))):
            max = i*j
print(max)