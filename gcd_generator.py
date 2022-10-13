
# The Euclids Division Lemma is "a = bq + r"

def getHCF(x, y):
  a = int(x)
  b = int(y)
  q = int(a // b)
  r = int(a % b)
  
  print('\nSteps\n')
  # Printing the euclids division lemma
  print(a, '=', b, '*', q, '+', r) 

  while r != 0:
    temporary_a = int(b)
    temporary_b = int(a % b)
    q = int(temporary_a // temporary_b)
    r = int(temporary_a % temporary_b)
    a = temporary_a
    b = temporary_b
    print(a, '=', b, '*', q, '+', r)
    
    if r == 0:
      print("\nThe HCF is", str(b))
      exit(0)

    
  
x = int(input('Please enter the first number - '))
y = int(input('Please enter the second number - '))

getHCF(x, y)