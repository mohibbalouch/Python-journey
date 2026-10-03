python_students = {"Ali", "Ahmed", "Sara", "Usman", "Zain"}
java_students = {"Ahmed", "Usman", "Zain", "Hassan", "Bilal"}

both_courses = python_students.intersection(java_students)
all_students = python_students.union(java_students)
only_python = python_students.difference(java_students)
only_java = java_students.difference(python_students)

print("Students in both courses:", both_courses)
print("All students:", all_students)
print("Only Python:", only_python)
print("Only Java:", only_java)
