import random


big_list = [random.randint(1, 10) for _ in range(200)]


def count_num(numbers):
    num_dict = {num: numbers.count(num) for num in set(numbers)}
    return num_dict


def plural(number):
    if 10 > number > 20:
        plural_num = int(str(number)[-1])
        return plural_num
    else:
        return number


right_form = lambda x: "раз" if x == 1 else "рази" if 1 < x < 5 else "разів"


result = count_num(big_list)
correct_result = sorted(result.items())

for key, value in correct_result:
    print(f'Число {key} зустрічається {value} {right_form(plural(value))}')
