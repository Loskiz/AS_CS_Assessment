def StringClean(MyStr):
    OutString=''
    for i in MyStr:
        if i>='a' or i<='z':
            OutString+=i
    return OutString