word = b'r\xc3\xa9sum\xc3\xa9'
dec_word = word.decode()
print(dec_word)
lat_code = dec_word.encode('Latin-1')
print(lat_code)
fin_code = lat_code.decode('Latin-1')
print(fin_code)
