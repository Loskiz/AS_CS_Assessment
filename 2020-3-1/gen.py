#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:23:31 2020

@author: zhangletian
"""
index=0
l=[]
st='''0101001110110001110110001001110010110010101100011011000100010100'''
for i in range(8):
    l1=[]
    for j in range(8):
        l1.append(st[index])
        index+=1
    l.append(l1)
print(l)
        