value = [1, 2, '3', 'forth', 'end', 99, True, None]

new_list = list(map(lambda val: str(val) if isinstance(val, int) and not isinstance(val, bool) else val, value))

print(new_list)
