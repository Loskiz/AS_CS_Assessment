#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 19:12:13 2020

@author: zhangletian
"""

message='24567'


def calc_checksum(message):
    total1,total2=0,0
    for i in range(len(message)):
        
    
        total1+=int(message[i])
        total2+=int(message[i])*i
    st1=str(total1)
    st2=str(total2)
    checksum=st1[-1]
    staircheck=st2[-1]
    tcs=checksum+staircheck
    return tcs

def cmp(msg1,msg2):
    if calc_checksum(msg1)==calc_checksum(msg2):
        print('unchanged')
    else:
        print('changed')

msg1='46756'

msg2='28756'
msg3='45756'

cmp(msg1,msg2)
cmp(msg1,msg3)
print(calc_checksum(msg1))
print(calc_checksum(msg2))