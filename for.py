'''All about for loops.'''

# testing range outputs
def range_test():
    for i in range(1,10):
        print(i)
    for i in range(1,10,2):
        print(i)
    for i in range(10,1,-1):
        print(i)

# range_test()

# for loop with strings
def string_for():
    for i in str(input("Enter a value: ")):
        print(i)

# string_for()

# factorial calculator
def factorial(n:int):
    store = 1
    for i in range(1,n+1):
        store=store*i
        print(store)
    print(store)

# factorial(int(input("Enter a non negative number: ")))