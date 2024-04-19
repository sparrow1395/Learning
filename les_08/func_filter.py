value = ('Країна', 'шалаш', 'Летел', 'вертольот', 'УЧУ', 'мем', 'мова')

print(list(filter(lambda val: val.upper()[::-1] == val.upper()[::], value)))
