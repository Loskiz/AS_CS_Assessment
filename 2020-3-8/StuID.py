#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 23:44:40 2020

@author: zhangletian
"""

def GetInfo():
    Valid=False
    while Valid==False:
        UserID=input('ID: ')
        if len(UserID)==5 and 65<=ord(UserID[0])<=90:
            Valid=True
        PN=input('PN: ')
        result=UserID+"*"+PN
        return result

def TopLevel():
    Opt='Y'
    while Opt=='Y':
        l=GetInfo()
        r=WriteInfo(l)
        if r==False:
            break
        Opt=input("'Y' to continue, 'N' to quit: ")
    
def WriteInfo(l):
    with open('IDfile.txt','w') as f1:
        f1.write(l+'\n')
    return True

TopLevel()