def clean(mystr):
    result=''
    afterspace=True
    for i in mystr:
        if i!=' ':
            result+=i
            afterspace=False
        elif i==' ':
            if afterspace==False:
                result+=i
            afterspace=True
    print(result)
clean('   AA  BBB  C f')