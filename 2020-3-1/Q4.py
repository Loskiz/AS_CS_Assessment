#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 20:07:34 2020

@author: zhangletian
"""

def switch(weight):
    if weight == 3:
        weight=1
    else:
        weight=3
    return weight
weight=1
total=0

for i in range(12):
    digit=int(input('digit: '))
    value=digit*weight
    total+=value
    weight=switch(weight)
r=total%10
c=10-r
print('校验码为: ')