courses = ["Software Engineering", "java", "Internet", "C++"]
courses_2 = ["Art", "Ed"]
courses.extend(courses_2)
courses.insert(0, courses_2)
a = courses.pop()

for index, course in enumerate(courses):
    print(index, course)
