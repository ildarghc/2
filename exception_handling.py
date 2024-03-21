def string_to_int(s): # добавить обработку ValueError
   try:
       return int(s)
   except ValueError as exc:
       return f'Ошибка {exc}: невозможно преобразовать {s} в целое число'

def read_file(filename): # добавить обработку FileNotFoundError, IOError
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError as exc:
        return f'Ошибка {exc}: файл {filename} не найден'
    except IOError as file:
        return f'Ошибка {exc}: ошибка при открытии файла {filename}'

def divide_numbers(a, b): # добавить обработку ZeroDivisionError, TypeError
    try:
        return a / b
    except ZeroDivisionError as exc:
        return f'Ошибка {exc}: делить на 0 нельзя'
    except TypeError as exc:
        return f'Ошибка {exc}: несовместимость операции (деление) с объектами (не числа)'
def access_list_element(lst, index): # добавить обработку IndexError, TypeError
    try:
        return lst[index]
    except IndexError as exc:
        return f'Ошибка {exc}: индекс {index} вне диапазона списка {lst}'
    except TypeError as exc:
        return f'Ошибка {exc}: индекс должен быть целым числом'

# print(string_to_int('1'))
# print(string_to_int('i'))
#
# print(read_file('text.txt'))
# print(read_file('text2.txt'))
#
# print(divide_numbers(0, 1))
# print(divide_numbers(1, 0))
# print(divide_numbers('a', 'b'))
#
# print(access_list_element([0,1,2], 1))
# print(access_list_element([0,1,2], 3))
# print(access_list_element([0,1,2], 'a'))



