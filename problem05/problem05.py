# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 22:20:11 2019

@author: samet
"""
# i=2520*11*13*17*19;
def twenty(num):
    j=11
    ch=0
    while(j<=20):
        if(num%j==0):
            ch+=1
        j+=1
    return ch        
# i=2520*11*13*17*19 first multiplied by prime numbers
i=116396280
while twenty(i)!=10:
    i+=1
print(i)