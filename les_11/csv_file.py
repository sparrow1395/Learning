import json
import csv
import random

with (open('students.json', 'r')) as f:
    value = json.load(f)

mob_op = random.choice(['095', '066', '098', '096', '050', '097'])
top = ['ID', 'Name', 'Age', 'Phone']
main_data = []
for code, info in value.items():
    lucky = random.choices([True, False], weights=[0.75, 0.25])[0]
    number = mob_op + str(random.randint(1000000, 9999999)) if lucky else ""
    data = [code, info[0], info[1], number]
    main_data.append(data)
with open("students.csv", 'w', newline="", encoding='utf-8') as f:
    write = csv.writer(f, delimiter=',')
    write.writerow(top)
    write.writerows(main_data)
