def choose():
    Choice=input('''
Add a new book to the text file, press 1
Search for books written by a given author, press 2
End the program, press 3
Your choice: ''')
    return Choice

def addNewBlock():
    Name=input('Please input the author name: ')
    Title=input('Please input the book title: ')
    Line=''+Name+', '+Title
    with open('BookInfo.txt','a') as f1:
        f1.write(Line)

def searchByAuthor():
    SC=input('Please input the name of the author: ')
    with open('BookInfo.txt') as f2:
        for i in f2:
            SdtIndex=0
            NameText=''
            titles=[]
            for j in i:
                if j!=',':
                    NameText+=j
                    SdtIndex+=1
                    
                else:
                    break
                    print(NameText)
            if SC==NameText:
                Out2=''
                flg=False
                for k in i[SdtIndex+2:-1]:
            
                    if flg==False:
                        if k==' ':
                            continue
                    flg=True
           
                    Out2+=k
                print(Out2)
                Found=True
                break
           
        if Found!=True:
            print('No books')
                
while 1:
    Choice=choose()
    if Choice=='1':
        addNewBlock()
    elif Choice=='2':
        searchByAuthor()
    elif Choice=='3':
        break
    else:
        print('Invalid input')
