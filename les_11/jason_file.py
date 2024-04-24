import json

student = {
    432647: ('John', 34),
    578301: ('Brian', 45),
    409786: ('Sam', 21),
    557890: ('Lisa', 30),
    199513: ('Bjorn', 35),
    451666: ('Sting', 40)
}

with open('students.json', 'w') as f:
    json.dump(student, f)

with open('students.json') as f:
    a = json.load(f)

print(type(a))
