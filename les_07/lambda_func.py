a = int(input("Enter your number: "))
odd_not = lambda x: "its zero" if x == 0 else ("its odd" if x % 2 == 0 else "Its not odd")

print(odd_not(a))
