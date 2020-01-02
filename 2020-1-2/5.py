with open('LoginEvents.txt') as f:
    LoginEvents=[]
    UserID=input('ID: ')
    for i in f:
        
        if f[0:4]==UserID:
            LoginEvents[0].append([i[5:8],i[9:24]])
        