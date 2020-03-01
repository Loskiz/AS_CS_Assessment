#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 14:01:12 2020

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
        return 'correct'
    else:
        return 'incorrect'

def checkrows(db):
    for i in range(len(datablock)):
        result=checkparity(db[i])
        if result=='incorrect':
            return i
    
def checkcolumns(db):
    l=[]
    for j in range(len(datablock[1])):
        for i in range(len(datablock)):
        
            l.append(db[i][j])
        result=checkparity(l)
        if result=='incorrect':
            return j

def flip(num):
    if num=='0':
        num='1'
    else:
        num='0'
    return num

def flipped(datablock,row,column):
    datablock[row][column]=flip(datablock[row][column])
    return datablock

index=0
datablock=[]
st='''0001001110110001110110001001110010110010101100011011000100010100'''
for i in range(8):
    l1=[]
    for j in range(8):
        l1.append(st[index])
        index+=1
    datablock.append(l1)


row=checkrows(datablock)
column=checkcolumns(datablock)
datablock=flipped(datablock,row,column)
print(datablock)