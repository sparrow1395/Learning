val_1 = input("Enter your first string: ")
val_2 = input("Enter your second string: ")
val_3 = input("Enter your third string: ")
val_4 = input("Enter your fourth string: ")

with open ("check.txt", "w") as f:
    f.write(val_1 + "\n")
    f.write(val_2 + "\n")
with open("check.txt", "a") as f:
    f.write(val_3 + "\n")
    f.write(val_4 + "\n")
