def ValidatePassword(Password):
    lower=0
    upper=0
    num=0
    Valid=False
    for i in Password:
        if 48<=ord(i)<=57:
            num+=1
        elif 65<=ord(i)<=90:
            upper+=1
        elif 97<=ord(i)<=122:
            lower+=1
        else:
            break
    if upper>=2 and lower>=2 and num>=3:
        Valid=True
    return Valid
Password=('111AAcc')
a=ValidatePassword(Password)
print(a)