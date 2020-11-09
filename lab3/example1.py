number = int(input("Please enter an integer:\n"))
if number < 10:
  total = number
else:
  ones = number%10
  tens = (number//10)%10
  total = ones + tens
print("Sum of the last two digits: ", total)