def share_diagonal(x0, y0, x1, y1):
    m=abs((y1-y0)/(x1-x0))
    return m==1

def col_clashes(pre_col,col):
    for i in range(col):
        if share_diagonal(i,pre_col[i],col,pre_col[col]):
            return True
    return False

def has_clahses(bd):
    for col in range(1,len(bd)):
        if col_clashes(bd, col):
            return True
    return False

import random
import copy
import math
n=int(input('Please input the size of the qipan: '))

rng=random.Random()

bd=list(range(n))
num_found=0
tries=0

a1=[]
while tries<=math.factorial(n)*2:
#while num_found<=65535:
    rng.shuffle(bd)
    a2=copy.deepcopy(bd)
    
    tries+=1
    if not has_clahses(a2) and a2 not in a1:
        a1.append(a2)
        print("Found solution {} in {} tries.".format(a2, tries))
        tries =0
        num_found+=1

