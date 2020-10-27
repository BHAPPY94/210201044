month = input("Enter month: \n")
day = int(input("Enter day: \n"))
if month == "March" or month == "April" or month == "May":
  if month == "March" and day < 21:
    print ("Winter")
  else:
    print ("Spring")
elif month == "June" or month == "July" or month == "August":
  if month == "June" and day < 21:
    print ("Spring")
  else:
    print ("Summer")
elif month == "September" or month == "October" or month == "November":
  if month == "September" and day < 23:
    print ("Summer")
  else:
    print ("Fall")
elif month == "December" or month == "January" or month == "February":
  if month == "September" and day < 21:
    print ("Fall")
  else:
    print ("Winter")