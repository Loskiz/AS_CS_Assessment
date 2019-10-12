def GetTemp(sensor):
    return 26

def Alarm():
    print('ALARM')

def CheckSensor():
    while 1:
        id=input("Please input the sensor ID: ")
        a=[]
        for i in range(1,11):
            a.append(i)
        if id in a:
            break
    LowTemp=20
    HighTemp=40
    temp=GetTemp(id)
    if temp<LowTemp:
        print('Cold')
    elif temp>HighTemp:
        Alarm()
    else:
        print('Normal')

CheckSensor()