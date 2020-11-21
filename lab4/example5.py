numbers = int(input("Enter how many numbers:\n"))
fibo = [1,1]
if numbers > 2:
  for i in range(2, numbers):
    nextElement = fibo[i-1] + fibo[i-2]
    fibo.append(nextElement)
print(fibo)