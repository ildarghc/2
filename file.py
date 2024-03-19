# print(ord('h'))
# print(chr(104))
#
# for ch in 'hello':
#     print(ord(ch))
#
# codes = [104, 101, 108, 108, 111]
# out = ''
# for code in codes:
#     out += chr(code)
# print(out)


# file = open('text.txt', mode='r', encoding='utf8')
# print(file.read())
# file.close()

# print(file.name)
# print(file.mode)
# print(file.encoding)
# print(file.closed)
#
# print(file.readable())
# print(file.writable())
# print(file.seekable())
# # print(file.truncate(size=None))
# print(file.flush())

#-------------------------------------------------------------------
# Форматирование строк
# print('{txt:*^30}'.format(txt='строка'))
#
# txt = 'строка'
# print(f'{txt:*^30}')
#
# var_1 = 34
# print(f'Удвоеннное значение переменной - {var_1 * 2:*^10d}')
#
# my_list = [1,2,3132457,4,5]
# print(f'Операции с третьим элементом списка - {round(my_list[2] / 3, 3):*^30.3f}')
#
# my_dict = {'a': 1, 'b': 2}
# print(f"Значение словаря - {my_dict['a']:*^10d}")
#
# file_name = 'out.txt'
# var_1 = 42
# with open(file_name, mode='w', encoding='utf8') as file:
#     file.write('Вывод числа %d' % (34, ))
#     file.write('\n')
#     file.write('Мы - те {}, что говорят "{}!"'.format('рыцари', 'Ха'))
#     file.write('\n')
#     file.write(f'Значение переменной var_1 - {var_1:<10d}')
#     file.write('\n')

#-------------------------------------------------------------------

# Файлы в операционнной системе
# import os, time
#
# path = 'C:/Windows/Help'
# path_normalized = os.path.normpath(path)
# print(path_normalized)
#
# count = 0
# for dirpath, dirnames, filenames, in os.walk(path_normalized):
#     print('*' * 27)
#     print(dirpath, dirnames, filenames)
#     print(os.path.dirname(dirpath))
#     count += len(filenames)
#     for file in filenames:
#         full_file_path = os.path.join(dirpath, file)
#         secs = os.path.getmtime(full_file_path)
#         file_time = time.gmtime(secs)
#         if file_time[0] == 2013:
#             print(full_name_path, secs, file_time)
# print(count)
# print(__file__, os.path.dirname(__file__))

import zipfile
from pprint import pprint
from random import randint

# zip_file_name = 'voyna-i-mir.txt.zip'

# zfile = zipfile.ZipFile(zip_file_name, 'r')
# zfile.printdir()
# for filename in zfile.namelist():
#     print(filename)
#     zfile.extract(filename)

filename = 'voyna-i-mir.txt'

stat = {}
# stat = {'a': {'т': 500, 'х': 5, }, 'т':{'О': 100, 'У': 50, }, }

sequence = ''
with open(filename, 'r', encoding='cp1251') as file:
    for line in file:
        # print(line)
        for char in line:
            if sequence in stat:
                if char in stat[sequence]:
                    stat[sequence][char] += 1
                else:
                    stat[sequence][char] = 1
            else:
                stat[sequence] = {char: 1}
            sequence = sequence [1:] +  char

pprint(stat)
pprint(len(stat))

totals = {}
stat_for_generate = {}
for sequence, char_stat in stat.items():
    totals[sequence] = 0
    stat_for_generate[sequence] = []
    for char, count in char_stat.items():
        totals[sequence] += count
        stat_for_generate[sequence].append([count, char])
    stat_for_generate[sequence].sort(reverse=True)

pprint(totals)
pprint(stat_for_generate)

N = 1000
printed = 0

sequence = ''
while printed < N:
    char_stat = stat_for_generate[sequence]
    total = totals[sequence]
    dice = randint(1, total)
    pos = 0
    for count, char in char_stat:
        pos += count
        if dice <= pos:
            break
    print(char, end='')
    printed += 1
    sequence = sequence [1:] +  char