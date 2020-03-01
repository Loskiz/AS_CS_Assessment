#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 13:54:36 2020

@author: zhangletian
"""

def checkparity(datum):
    ones=0
    even=False
    for i in datum[1:]:
        if i=="1":
            ones+=1
    if ones%2==0:
        even=True
    else:
        even=False
    if datum[0]=='0':
        parity=True
    else:
        parity=False
    if parity==even:
        return 'corrct'
    else:
        return 'incorrct'

print(checkparity('100001100'))
print(checkparity('100001101'))