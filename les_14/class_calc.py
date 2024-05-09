class NegativeNumber(Exception):
    pass


class Calculator:
    @staticmethod
    def plus(a, b):
        try:
            return a + b
        except TypeError:
            print("You can not add str to int, sorry")
        except OverflowError:
            print("C'mon im not so smart")

    @staticmethod
    def minus(a, b):
        try:
            return a - b
        except TypeError:
            print("You can not subtract str and int, sorry")
        except OverflowError:
            print("C'mon im not so smart")

    @staticmethod
    def divide(a, b):
        try:
            return a / b
        except TypeError:
            print("You can not divide str and int, sorry")
        except ZeroDivisionError:
            print("No WAY, how did you forgot the basics")

    @staticmethod
    def multi(a, b):
        try:
            return a * b
        except TypeError:
            print("How do you think we can multiply letters or str symbols?")
        except OverflowError:
            print("C'mon im not so smart")

    @staticmethod
    def power(a, b):
        try:
            return a ** b
        except TypeError:
            print("It's impossible")
        except OverflowError:
            print("C'mon im not so smart")

    @staticmethod
    def root(a):
        try:
            res = a * 0.5
            return res
        except TypeError:
            print("Check again what yous sent to me")
        except OverflowError:
            print("C'mon im not so smart")


Calculator.plus(5, "a")
