import openpyxl
import csv

data = []
with open("students.csv") as file:
    val_stud = csv.reader(file)
    for row in val_stud:
        data.append(row)
for row in data:
    del row[2]

wb = openpyxl.Workbook()
sheet = wb.active

for row_ind, row_dat in enumerate(data):
    for col_ind, value in enumerate(row_dat):
        cell = sheet.cell(row=col_ind + 1, column=row_ind + 1)
        cell.value = value
wb.save("students.xlsx")
