with open('PRODUCTS2.txt') as f2:
    SPC=0
    PCode=[]
    PDescription=[]
    PRetailPrice=[]
    a2=f2.readlines()
    for i in a2:
        temp=''
        for j in i:
            
            if not(j=='#' or j=='\n'):
                temp+=j
                #print(temp)
            else:
                if SPC==0:
                    PCode.append(temp)
                    #print(temp)
                    temp=''
                    SPC+=1
                    
                elif SPC==1:
                    PDescription.append(temp)
                    print(temp)
                    temp=''
                    SPC+=1
                elif SPC==2:
                    PRetailPrice.append(temp)
                    temp=''
                    SPC=0
            
print(PCode,PDescription,PRetailPrice)
#print(temp)