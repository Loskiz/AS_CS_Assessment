def ProcessMarks(Marks):
    Highest=0
    total=0
    index=0
    for i in range(len(Marks)):
        if Marks[i] > Highest:
            Highest=Marks[i]
            index=i
        total+=i
    avg=total/len(Marks)
    print('avg is',avg,'highest is',Highest)
    return index
Marks=[1,2,3,4,5,6,7,8,9,10]
a=ProcessMarks(Marks)
print(a)

        