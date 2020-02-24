def FindRepeats(arr):
    repeats=0
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            print(arr[i])
            repeats+=1
