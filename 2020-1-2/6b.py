picture=[[222,222,222,222,222],[111,111,111,111,111],[99,99,99,99,99]]
def Lighten():
    global picture
    Flag=False
    for i in range(len(picture)):
        for j in range(len(picture[i])):
            picture[i][j]*=1.1
            picture[i][j]=int(picture[i][j])
            if picture[i][j]>=255:
                Flag=True

    print(picture)
    return Flag
a=Lighten()
print(a)
