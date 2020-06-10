# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Point:

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def halfway(self, target):
         mx = (self.x + target.x) / 2
         my = (self.y + target.y) / 2
         return Point(mx, my)
     
    def distanceFromPoint(self,target):
        return ((self.x-target.x)**2+(self.y-target.y**2)) ** 0.5
    
    def reflect_x(self):
        return (self.x,-(self.y))
    
    def slope_from_origin(self):
        if self.x==0  or self.y==0:
            return None
        return(self.y/self.x)
    
    def get_line_to(self,target):
        m=(self.y-target.y)/(self.x-target.x)
        c=self.y-m*self.x
        return (m,c)
    
    def move(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy
        
def find_PBi(p1,p2):
    h1=p1.halfway(p2)
    line=p1.get_line_to(p2)
    m1=-(1/line[0])
    c1=h1.y-m1*h1.x
    return (m1,c1)
    
def find_intersect(l1,l2):
    x=(l2[1]-l1[1])/(l1[0]-l2[0])
    y=l1[0]*x+l1[1]
    p=Point(x,y)
    return p
    
def find_circle(p1,p2,p3):
    h1 = find_PBi(p1,p2)
    h2 = find_PBi(p2,p3)
    c=find_intersect(h1,h2)
    return (c,c.distanceFromPoint(h1))

def find_circle4(p1,p2,p3,p4):
    h1 = find_PBi(p1,p2)
    h2 = find_PBi(p2,p3)
    c=find_intersect(h1,h2)
    return (c,c.distanceFromPoint(h1))