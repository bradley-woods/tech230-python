# Dictionaries

# Dictionaries work using key/value pairs

# key = reference to an object
# value = data stored in said object

student_1 = {
    "name": "Bradley",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "set_up"]
}

student_2 = {
    "name": 1,
    "stream": 2,
    "completed_lessons": 3,
    "completed_lesson_names": 4
}
#
# print(type(student_1))
# print(student_1["completed_lesson_names"][0])
#
# # changing a value
# student_1["completed_lessons"] = 3
# print(student_1["completed_lessons"])
#
# # changing a value in a list, within a dictionary
# student_1["completed_lesson_names"].remove("set_up")
# print(student_1["completed_lesson_names"])

# Dictionary methods

print(student_1.keys())
print(student_1.values())
print(student_1.items())

print(type(student_1.keys()))
print(type(student_1.values()))
print(type(student_1.items()))

print(sum(student_2.values()))
