student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
  "Draco": 54,
}

print(''' \n \n                                     888                             
                             888                             
                             888                             
88888b. 888  88888888b.d88b. 88888b.  .d88b. 888d888.d8888b  
888 "88b888  888888 "888 "88b888 "88bd8P  Y8b888P"  88K      
888  888888  888888  888  888888  88888888888888    "Y8888b. 
888  888Y88b 888888  888  888888 d88PY8b.    888         X88 
888  888 "Y88888888  888  88888888P"  "Y8888 888     88888P \n ''' )

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Covert scores into grades.
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
    
print(student_grades)