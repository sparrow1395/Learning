import random
from colorama import Fore
from datetime import datetime
values = list(random.randint(1, 100) for _ in range(200))


def decorator(func):
    def wrapper(*args):
        t_speed = 0
        for _ in range(200):
            start = datetime.now()
            func(*args)
            finish = datetime.now()
            t_speed += (finish - start).total_seconds() * 1000

        av_speed = t_speed / 200
        print(Fore.LIGHTGREEN_EX + f'"Speed of this function is {str(av_speed)} ms"')
    return wrapper


@decorator
def calculating(varia):
    from functools import reduce
    result = reduce(lambda a, b: a + b, varia, 0)
    print(Fore.LIGHTCYAN_EX + str(result))
    return result


@decorator
def filtering(varia):
    odd = filter(lambda num: num % 2 == 0, varia)
    print(Fore.LIGHTCYAN_EX + str(list(odd)))
    return odd


calculating(values)
filtering(values)
