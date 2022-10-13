ip=int(input("Enter a number: "))

for n in range(2, ip):
    r=ip%n
    if r==0:
        print("This is not a prime number")
        exit(0)
else:
    print("This is a prime number")