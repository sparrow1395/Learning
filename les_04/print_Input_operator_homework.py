# print/input

sentence = input('Enter your sentence: ')

# Here im splitting sentence into words and marking this words by a variable

first_word = sentence.split()[0]
second_word = sentence.split()[1]

print(sentence, end="<<<>>>")
print('!{} {}?'.format(second_word.upper(), first_word.capitalize()), end='<<<>>>')
print('!%s %s?' % (second_word.upper(), first_word.capitalize()), end='<<<>>>')
print(f'!{second_word.upper()} {first_word.capitalize()}?')
