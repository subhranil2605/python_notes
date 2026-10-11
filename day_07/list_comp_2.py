students = [
    ["Rutuja", 26],
    ["Raj", 28],
    ["Subhranil", 27],
    ["Pratiksha", 27],
]

# Get the students whose age is greater than 26 and store them in a new list

# new_students = []
# for student in students:
#     age: int = student[1]

#     if age > 26:
#         new_students.append(student)

# print(new_students)


# new_students = list(filter(lambda x: x[1] >= 26, students))
# print(new_students)

# list comprehension: create a copy of the list
# new_students = students[:]
# new_students = [student for student in students]
# print(new_students)

new_students = [student for student in students if student[1] > 26]
print(new_students)
