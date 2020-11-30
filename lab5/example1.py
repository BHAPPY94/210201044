mail = input("Please enter your e-mail address:\n")
ref_mail = "ceng113@example.com"
if "@" in mail:
  mail = mail.lower()
  part1 = mail.split("@")[0]
  part1 = part1.replace(".", "")
  part2 = mail.split("@")[1]
  mail = part1 + "@" + part2
  print(mail)

  if mail == ref_mail:
    print("Equal")
  else:
    print("Not equal")

else:
  print("Not equal")