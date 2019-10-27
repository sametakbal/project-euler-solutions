# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:23:39 2019

@author: samet

Bütün asal sayılar 6n+1 veya 6n-1 kuralına uyar. 2 ve 3 hariç. Köküne kadar bölümüyorsa sayı asaldır.

All prime numbers follow the 6n+1 or 6n-1 rule. Except 2 and 3. and prime if the number is not divided by until its root
"""
def check_prime(num):
    i=2
    while(i<=(num**(0.5))):
        if num % i == 0:
            return False
        i+=1
    return True
arr= []
arr.append(2)
arr.append(3)
count=2
i=1
while(count<10001):
    if check_prime(i*6+1):
        arr.append(i*6+1)
        count+=1
    if check_prime(i*6-1):
        arr.append(i*6-1)
        count+=1
    i+=1
print(arr.pop())