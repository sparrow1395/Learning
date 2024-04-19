n = int(input("Enter your number: "))

result = 0

for cube in range(1, n+1):
    if cube % 3 != 0:
        result += cube**3
print(result)

# result = [i ** 3 for i in range(1, n+1) if i % 3 != 0]
# result_2 = sum(result)
# print(result_2)
