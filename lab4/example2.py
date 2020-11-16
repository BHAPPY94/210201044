N = int(input("How many numbers?\n"))
even = 0
for i in range(N):
  number = int(input("Enter an integer:\n"))
  if number%2==0:
    even += 1 
percentage = even/N*100
print (percentage, "%")