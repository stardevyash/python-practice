ip=str(input("Enter number: "))

num=""

for t in ip:
    num=t+num

if num == ip:
    print("this is a palendrome")

else:
    print("this isn't a palendrome")