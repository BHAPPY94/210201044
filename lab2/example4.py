age = int(input("Enter your age:\n"))
ticket_price = 3
if age <6 or age >60:
  ticket_price = 0
  print ("Free! Your payment is:", ticket_price)
elif age>=6 and age<18:
  ticket_price = 3 * 0.5
  print ("Your payment is:", ticket_price)
elif age >=18 and age <= 60:
  print ("Your payment is:", ticket_price)