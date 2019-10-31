while 1:
    TicketType= input('Please input the type of your ticket: ')
    if TicketType=='E' or TicketType=='S':
        break
    else:
        print("A valid ticket type would be 'E' or 'S' ")
BaggageWeight=float(input('Please input the weight of the baggage: '))
if TicketType== 'E':
    ChargeRate=3.5
    BaggageAllowance=16
else:
    ChargeRate=5.75
    BaggageAllowance = 20
ExcessWeight=BaggageWeight-BaggageAllowance
if ExcessWeight>0:
    charge=ExcessWeight*ChargeRate
else:
    charge=0
print(charge)