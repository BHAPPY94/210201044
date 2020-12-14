a = int(input("Enter an integer:\n"))
b = int(input("Enter an integer:\n"))

def is_prime(a):
  if a > 1:
   for i in range(2,a):
       if (a % i) == 0:
           print(a,"is not a prime number")
           print(i,"times",a//i,"is",a)
           break
   else:
       print(a,"is a prime number")       
  else:
   print(a,"is not a prime number")
  return a

def print_primes_between(a,b):
  a=5
  return a