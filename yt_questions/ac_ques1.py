'''Solution to question at https://youtube.com/shorts/XF4l1T8kLUo?feature=share'''

doors=range(1,101)
monkeys=range(1,101)

opend=[]

for d in doors:
    factors=0
    for m in monkeys:
        rem=d%m
        if rem==0:
            factors+=1
    if factors%2==1:
        opend.append(d)

print("The number of open doors are: ", str(len(opend)))
print("The open doors are: ", opend)