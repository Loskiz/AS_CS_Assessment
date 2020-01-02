def AddNewScores():
    Date=input('DDMMYY: ')
    while 1:
        MemNum=input('MemNum: ')
        if MemNum=='':
            break
        Score=input('Score: ')
        while not 50<=int(Score)<=99:
            Score=input('Score: ')
        Str=MemNum+Date+Score
        print(Str)
        with open('ScoreDetials.txt','a') as f:
            f.write(Str)
AddNewScores() 