with open('PRODUCTS.txt') as f:
    PCode=[]
    PDescription=[]
    PRetialprice=[]
    a=f.readlines()
    for i in range(0,len(a)-2,3):
        PCode.append(a[i][:-2])
        PDescription.append(a[i+1][:-2])
        PRetialprice.append(float(a[i+2][:-2]))
print(PCode,PDescription,PRetialprice)