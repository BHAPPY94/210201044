static_password = "abc123"

while True:
  password = input("Enter password: ")
  if password==static_password:
    print("Welcome")
    break
  elif password =="help":
    print(static_password[0],"is the first letter of password")
  else:
    print("Wrong")