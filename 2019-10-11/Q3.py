def ScanArray(ArrayName):
    total=0.0
    AverageValue=0
    ZeroCount=0
    for i in ArrayName:
        total+=i
        if i == 0:
            ZeroCount+=1
    AverageValue=total/100
    print('Average value is {}'.format(AverageValue))
    print('Zero count is {}'.format(ZeroCount))

a=[2 for i in range(99)]
a.append(0)
ScanArray(a)