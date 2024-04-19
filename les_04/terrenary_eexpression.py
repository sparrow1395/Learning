# Homework for terrenary
num = input('Введіть число: ')
if (bool(int(num))) is False:
    print('Це нуль')
elif num.strip('-').isdigit():
    num2 = int(num)
    even_odd = 'парне' if int(num2) % 2 == 0 else 'непарне' if abs(int(num2)) % 2 != 0 else 'Нуль'
    print('Ви ввели {0} число'.format(even_odd))
else:
    print('Не вірнe ввeдення')
