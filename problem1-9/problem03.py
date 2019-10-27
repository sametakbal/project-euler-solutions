# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 21:38:40 2019

@author: samet
"""
num=600851475143
div=2
while(num>1):
    if(num%div==0):
        num/=div
    else:
        div+=1
print(div)