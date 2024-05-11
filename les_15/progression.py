import time

start = int(input("Enter start number: "))
prog = int(input("Enter progression: "))


class MyClass():

    def __init__(self, start, prog):
        self.start = start
        self.prog = prog
        self.first = None

    def __next__(self):
        if self.first is None:
            self.first = self.start
            return self.first
        else:
            self.first *= prog
            return self.first

    def __iter__(self):
        return self


my_list = MyClass(start, prog)

while True:
    try:
        for item in my_list:
            print(item)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Not so fast, I WANT MORE NUMBERS HEHEHEHEH")

