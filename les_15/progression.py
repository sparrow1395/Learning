import time

start = int(input("Enter start number: "))
prog = int(input("Enter progression: "))

def progression (start, prog):
    current = 0
    if current == 0:
         current = start
         yield current
    while True:
        current *= prog
        yield current


generator = progression(start, prog)

while True:
    try:
        print(next(generator))
        time.sleep(1)
    except KeyboardInterrupt:
        print("Not so fast, I WANT MORE NUMBERS HEHEHEHEH")

