num1 = float(input("Enter number 1:\n"))
num2 = float(input("Enter number 2:\n"))
num3 = float(input("Enter number 3:\n"))
if num1 < num2:
  if num1 < num3:
    print (num1)
elif num2 < num3:
  print (num2)
else:
  print (num3)