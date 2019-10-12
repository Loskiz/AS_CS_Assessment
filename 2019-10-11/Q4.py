def AddToFile(StringName, FileName='ClassContact.txt'):
    with open(FileName,'a') as f1:
        f1.write(StringName)

def SearchFile(Name,File='StudentContact.txt'):
    with open(File) as f2:
        
        found=False
        for i in f2:
            temp=''
            for j in i:
                if j!='*':
                    temp+=j
                if j=='*':
                    break
            if temp == Name:
                found =True
                return i
        if found == False:
            return ''

def ProcessArray(File='ClassList.txt'):
    nonum=0
    Array=[]
    with open(File) as f2:
        Array= f2.readlines()

    for k in Array:
        StuInf=SearchFile(k[:-1])
        if StuInf != '':
            AddToFile(StuInf)
        else:
            AddToFile(k+'*No number')
            nonum+=1
    return nonum

z=ProcessArray()
print('Students with no number: {}'.format(z))
