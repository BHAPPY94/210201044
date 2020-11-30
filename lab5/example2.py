how_many_students = int(input("Enter how many students:"))
grades = []
for i in range(how_many_students):
  midterm1 = input("Enter midterm 1:")
  midterm2 = input("Enter midterm 2:")
  final = input("Enter final:")
  avg_midterm1 = midterm1 * 30/100
  avg_midterm2 = midterm2 * 30/100
  avg_final = final * 30/100
  grades.append(avg_midterm1)
  grades.append(avg_midterm2)
  grades.

  print()
  if midterm1 == "quit" or midterm2 == "quit" or final == "quit":
    break

