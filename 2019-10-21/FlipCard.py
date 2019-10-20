def SetUpEmptyGrid():
    Grid=[[0]*8 for i in range(8)]
    for j in range(8):
        for k in range(8):
            Grid[j][k]=0
    return Grid

def RandomlyDistributeCards(Grid):
    for num in range(1,33):
        x,y=GetEmptyGridPosition(Grid)
        Grid[x][y]=num
        x,y=GetEmptyGridPosition(Grid)
        Grid[x][y]=num
    return Grid

def GetEmptyGridPosition(Grid):
    import random as rd
    while 1:
        x=rd.randint(0,7)
        y=rd.randint(0,7)
        if Grid[x][y]==0:
            break
    return x,y

def SetUpPlayers():
    Points=[0,0]
    ThisPlayer=0
    return Points,ThisPlayer

def GetPlayerCoordinates(Grid):
    while 1:
        x1=int(input('Please input the x1 coordinate of the point: '))
        y1=int(input('y1 coordinate: '))
        if Grid[x1][y1]>0:
            break
    DisplayGrid(Grid,x1,y1)
    while 1:
        x2=int(input('Please input the x2 coodinates: '))
        y2=int(input('y2: '))
        if Grid[x2][y2]>0 and x2!=x1 and y2 != y1:
            break
    return x1,y1,x2,y2

def DisplayGrid(Grid,x1,y1):
    for i in range(8):
        for j in range(8):
            if i==x1 and j==y1:
                print(Grid[x1][y1],end='')
            elif Grid[i][j]==0:
                print('X',end='')
            else:
                print('?',end='')
        print('\n')
def TestForMatch(Grid,x1,y1,x2,y2,ThisPlayer,Points):
    if Grid[x1][y1]==Grid[x2][y2]:
        Grid[x1][y1]=0
        Grid[x2][y2]=0
        Points[ThisPlayer]+=1
    else:
        ThisPlayer=SwapPlayers(ThisPlayer)
    return Grid,Points

def SwapPlayers(ThisPlayer):
    if ThisPlayer==0:
        ThisPlayer=1
    else:
        ThisPlayer=0
    return ThisPlayer

def TestForEndGame(Points):
    GE=False
    if Points[0] + Points[1]==32:
        GE=True
    return GE

def OutPutResults(Points):
    print(Points[0])
    print(Points[1])

Grid=SetUpEmptyGrid()
Grid=RandomlyDistributeCards(Grid)
Points,ThisPlayer=SetUpPlayers()
GameEnd=False
while 1:
    x1,y1,x2,y2=GetPlayerCoordinates(Grid)
    DisplayGrid(Grid,x2,y2)
    Grid,Points=TestForMatch(Grid,x1,y1,x2,y2,ThisPlayer,Points)
    GameEnd=TestForEndGame(Points)
    if GameEnd==True:
        break
OutPutResults(Points)
