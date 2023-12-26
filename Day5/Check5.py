# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
i = 0
avg_height = 0
total_height = 0
for avg_height in student_heights:
  total_height += avg_height
  i += 1
 

print(total_height)