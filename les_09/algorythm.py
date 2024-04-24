def guess_num(inc):
    if inc == '0':
        return "It's zero"
    elif inc.lstrip('-').replace('.', '', 1).replace(',', '').isdigit():
        val = inc.replace(',', '.')
        num = float('0' + val) if val.startswith('.') else (float(val) if "." in val else int(val))
        b = "decimal" if "." in val else "integer"
        a = "positive" if num > 0 else "negative"
        return f"Thi number is {a} {b}: {num}"
    else:
        return f"You entered wrong number: {inc}"


while True:
    value = input("Enter your number: ").lower()
    if value in ['вихід', 'exit', 'quit', 'e', 'q']:
        break
    else:
        print(guess_num(value))
