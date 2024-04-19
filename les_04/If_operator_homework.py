# If operator

while True:
    name = input('Enter your name: ')
    age = input('Enter your age: ')

    if not age.isdigit() or int(age) <= 0:
        print('Помилка, повторіть введення')
        continue
    elif 0 < int(age) < 10:
        print('Привіт, шкет {}'.format(name))
    elif 10 <= int(age) <= 18:
        print('Як справи {}?'.format(name))
    elif 18 < int(age) < 100:
        print('Що бажаєте, {}?'.format(name))
    else:
        print('{} ви брешете у нас стільки не живуть '.format(name))

    exit_choice = input("Бажаєте вийти? (Д/Y): ").strip().upper()
    if exit_choice == "Д" or exit_choice == "Y":
        break
