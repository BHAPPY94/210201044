gpa = float(input("Enter your GPA:\n"))
lecture = int(input("Enter your lecture:\n"))
if gpa < 2.0:
  if lecture < 47:
    print ("Not enough number of lectures and GPA!")
  else:
    print ("Not enough GPA!")
else:
    if lecture < 47:
      print ("Not enough number of lectures!")
    else:
      print ("GRADUATED!")
