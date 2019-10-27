# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:14:22 2019

@author: samet
"""
square_sum=0
for i in range(1,101):
    square_sum+=i**2
sum_square=0
for i in range(1,101):
    sum_square+=i
sum_square**=2
print(sum_square-square_sum)