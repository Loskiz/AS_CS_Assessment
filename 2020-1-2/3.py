def GetTemp(SensorID):
    return 11
def Alarm():
    print('aaaaaaaaaaaaaafirefire')
def CheckSensor():
    SensorID=int(input('SensorID: '))
    while not 1<=SensorID<=10:
        SensorID=int(input('SensorID: '))
    Temp=GetTemp(SensorID)
    LowTemp=10
    HighTemp=20
    if Temp<LowTemp:
        print('Cold')
    elif Temp>HighTemp:
        Alarm()
    else:
        print('Normal')
CheckSensor()