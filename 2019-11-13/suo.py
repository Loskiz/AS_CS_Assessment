test='aaaaabbbcccccd'
def strencode(strz):
    temp=''
    new=''
    count=0
    for i in strz:
        if i!=new:
            if count!=0:
                temp+=str(count)+new
                count=0
            

            new=i
            count+=1
        else:
            count+=1
    temp+=str(count)+new
    return temp
a=strencode(test)
print(a)

t2='2t3r4g'    
def strdecode(str0):
    count=0
    index=0
    temp=''
    for i in str0:
        if count==0:
            try:

                index=int(i)
            except:
                ValueError
            count=1
        elif count==1:
            temp+=index*i
            count=0
    return(temp)
print(strdecode(t2))

    
            