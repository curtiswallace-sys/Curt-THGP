student_profile1 = {
"school": "Greenwood High",
    "name": "John Doe",
    "age": 16,
    "grade": "10th",
    "hobbies": ["Reading", "Chess", "Drawing"],
    "GPA": 4.0,
}

student_profile2 = {
"school": "Greenwood High",
    "name": "Emily Johnson",
    "age": 18,
    "grade": "12th",
    "hobbies": ["Basketball", "Gaming", "Cooking"],
    "GPA": 3.2,
}

student_profile3 = {
"school": "Greenwood High",
    "name": "Jamie Smith",
    "age": 17,
    "grade": "11th",
    "hobbies": ["Swimming", "Singing", "Camping"],
    "GPA": 2.8,
}

x = student_profile1.keys()
print(x)

y = student_profile2.values()
print(y)

z = student_profile3.get("name")
print(z)