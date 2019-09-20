#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:23:19 2019

@author: zhangletian
"""

#symbol of type string
#num_of_symbol of type int
#hang of type int
#temp of type int
symbol=input("Input a symbol: ")

while 1:
    num_of_symbol=int(input("Please input the number of symbol: "))
    if num_of_symbol%2==1:
        break
hang=num_of_symbol
temp=1
for i in range(1+hang//2):
    for j in range(1+num_of_symbol//2):
        print(' ',end='')
    for k in range(temp):
        print(symbol,end='')
    num_of_symbol-=2    
    temp+=2
    print('\n')