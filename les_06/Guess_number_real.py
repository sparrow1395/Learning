import random
ran_num = random.randint(1, 11)
print(ran_num)


def game(number1, number2):
    if number1 == number2:
        return True
    elif number1 > number2:
        print("my number is bigger")
    elif number1 < number2:
        print("my number is smaller")
    else:
        return False


def game_big():
    attempts = 0
    while attempts < 3:
        g_num = int(input("Enter number: "))
        attempts += 1
        if game(ran_num, g_num):
            print("Wow, you win!")
            return
    print(f"Game Over, the answer was {ran_num}")


def finish():
    close = input("Lets try again? (Y/N)")
    if close.upper() == "Y":
        return True
    elif close.upper() == "N":
        return False


while True:
    game_big()
    if not finish():
        break
