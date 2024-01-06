student = {"name": "John",
           "age": "23",
           "courses": ["Math", "Compsci"],
           } 
student["phone"] = "555-5555"
del student["phone"]
print(student.get("phone", "Not Found"))
print(student)