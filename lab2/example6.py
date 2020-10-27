a = float(input("Enter a:\n"))
b = float(input("Enter b:\n"))
c = float(input("Enter c:\n"))

delta = b**2 - 4 * a * c
if delta < 0:
    print("There are two complex roots")
elif delta == 0:
    print("There are one root")
else:
    print("There are two roots")
