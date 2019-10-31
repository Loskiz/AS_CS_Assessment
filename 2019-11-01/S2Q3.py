DHW=[5,10,10]
PD=[[10,11,10,14],[20,16,24,20],[9,11,13,17]]
WorkerTotal=[]
for i in DHW:
    WorkerTotal.append(0)
for j in range(3):
    for k in range(4):
        WorkerTotal[j]=WorkerTotal[j]+PD[j][k]

for m in range(3):
    WorkerAverage=WorkerTotal[m]/(4*(DHW[m]))
    if WorkerAverage<2:
        print('investigate',m+1)