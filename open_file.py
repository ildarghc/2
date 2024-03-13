file_name = 'text.txt'
file = open(file_name, mode='r', encoding='utf8')
print(file.read())
file.close()
