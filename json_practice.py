import json

student = [{
    "name": "David",
    "courses": "CPSC 231",
    "completed": False
},
{
    "name": "Jane",
    "courses": "MATH 265",
    "completed": True
}]

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

with open("student.json", "r") as file:
    loaded_student = json.load(file)

print(loaded_student)

