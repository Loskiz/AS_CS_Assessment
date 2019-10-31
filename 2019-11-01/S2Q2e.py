PCode=['2222','1111','3333']
def ProductCodeSearch(Code='2222',l=PCode):
    for i in range(len(PCode)):
        if PCode[i]==Code:
            return i
        
        else:
            return -1
print(ProductCodeSearch())
