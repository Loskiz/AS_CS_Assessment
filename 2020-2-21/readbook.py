with open('BookInfo.txt') as f1:
    Number=0
    titles=[]
    for i in f1:
        SdtIndex=0
        Number+=1
        if Number<10:
            OutNum='0'+ str(Number)
        else:
            OutNum=str(Number)
        OutText='#{} book author: '.format(OutNum)
        
        for j in i:
            if j!=',':
                OutText+=j
                SdtIndex+=1
            else:
                break
        OutText+=', book title:\"'
        Out2=''
        flg=False
        for k in i[SdtIndex+2:-1]:
            
            if flg==False:
                if k==' ':
                    continue
            flg=True
            OutText+=k
            Out2+=k
        titles.append(Out2)
        OutText+='\"'
        print(OutText)
Number=0
with open("BookInfo_new.txt",'w') as f2:
    for i in titles:
        Number+=1
        if Number<10:
            OutNum='0'+ str(Number)
        else:
            OutNum=str(Number)
        Line='#{} book title: \"'.format(OutNum)+i+'\", number of copies: {}'.format(ord(i[0]))+'\n'
        f2.write(Line)
