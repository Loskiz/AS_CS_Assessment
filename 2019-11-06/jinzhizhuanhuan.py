def jinzhizhuanhuan(num,orig,dest):
    a=list(str(num))
    temp=[]
    #print(a)
    a=list(reversed(a))
    for i in range(len(a)):

        a[i]=int(a[i])*int(orig)**i
        print(a)
    dec_num=sum(a)
    while dec_num!=0:
        
        if dec_num%dest!=0:

            temp.append(dec_num%dest)
        else:
            temp.append(0)
        dec_num=dec_num//dest
    #temp=temp.reverse()
    print(temp[::-1])
jinzhizhuanhuan(111111111111,2,10)


def lettonum(a):
    for i in range(len(a)):
        if a[i]=='a':
            a[i]='10'
        elif a[i]=='b':
            a[i]=='11'
        elif a[i]=='c':
            a[i]=='12'
        elif a[i]=='d':
            a[i]=='13'
        elif a[i]=='e':
            a[i]=='14'
        elif a[i]=='f':
            a[i]=='15'