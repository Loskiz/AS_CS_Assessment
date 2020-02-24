Lookup=['a','b']
StartIndex=int(input())
NumberToOutput=int(input())
Index=StartIndex
for i in range(NumberToOutput):
    OriginalChar=Decrypt(Lookup[Index])
    CipherChar=OriginalChar
    print('Index {}: Character {} has substitute character {}'.format(Index,OriginalChar,CipherChar))
