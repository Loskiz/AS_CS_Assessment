def OutPutTimeTable(num):
    
    for i in range(1,11):
        print('{} * {} = {}'.format(i,num,i*num))

num=int(input('Please input a number: '))
OutPutTimeTable(num)

def IsDivisible(n1,n2):
    if n1%n2==0:
        return True
    else:
        return False

a=IsDivisible(24,6)
b=IsDivisible(24,7)
print(a,b)

def  EggsIntoBoxes(NumberOfEggs):
    FilledBoxes=NumberOfEggs//6
    EggsLeftOver=NumberOfEggs%6
    return FilledBoxes,EggsLeftOver


