#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 10:29:34 2020

@author: zlt
"""


class Point2D(object):
    def __init__(self,x=0,y=0):
        self.X=x
        self.Y=y
    def GetX(self):
        return self.X
    def GetY(self):
        return self.Y
    def SetX(self,x):
        self.X=x
    def SetY(self,y):
        self.Y=y
    def Distance2Origin(self):
        return (self.X**2+self.Y**2)**0.5
    def Distance2otherPoint(self,p):
        return ((self.X-p.X)**2+(self.Y-p.Y)**2)**0.5
    def __str__(self):
        return '({},{})'.format(self.X,self.Y)
    
a=Point2D()
print(a)
b=Point2D(1,2)
print(b)
c=Point2D(2,2)
print(b.Distance2Origin())
print(b.Distance2otherPoint(c))
