# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 23:53:17 2019

@author: sametakbal
"""
# n. ucgensel sayi (n(n+1)) / 2 formulu ile bulunur.
#n. triangular number is found by the formula (n (n + 1)) / 2.

def divisor_counter(num):
    counter=1
    for i in range(2,num):
        if(num%i==0):
            counter+=1
    return counter+1


j = 10 #random value

while(divisor_counter(int((j*(j+1))/2))<500):
    j+=1
print((j*(j+1))/2)