def myand(a,b):
    if a == 1 and b==1:
        return 1
    else:
        return 0

def myor(a,b):
    if a==1 or b==1:
        return 1
    else:
        return 0

def myxor(a,b):
    if a!=b:
        return 1
    else:
        return 0

def bitadd(a,b):
    c=0
    r=myxor(a,b)
    if myand(a,b):
        c=1
    return r,c

def add(a,b):
    a=''.join(list(reversed(a)))
    b=''.join(list(reversed(b)))
    k=0
    thiscarry=0
    z=[]
    for i in range(len(a)):
        k=0
        k,nextcarry1=bitadd(int(a[i]),int(b[i]))
        #if thiscarry==1:
        k,nextcarry2=bitadd(k,thiscarry)
        thiscarry=myxor(nextcarry1,nextcarry2)
        z.append(k)
    z.append(myand(int(a[-1]),int(b[-1])))
    print(list(reversed(z)))
add('11111111','11111111')
        