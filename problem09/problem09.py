# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 22:54:27 2019

@author: samet
"""

for i in range(1,1000):
    for j in range(1,1000):
        tmp = (i**2)+(j**2)
        if i+j+(tmp**(0.5)) == 1000:
            print(i*j*(tmp**(0.5)))