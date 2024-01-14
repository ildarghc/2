def print_params(a=1, b='строка', c=True):
    print(a, b, c, sep=', ')


# Функция с параметрами по умолчанию:
print_params()
print_params(2)
print_params(2, 'другая строка')
print_params(2, 'другая строка', False)
print_params(b=25)
print_params(c=[1, 2, 3])


# Распаковка параметров:
values_list = [3, 'ещё строка', False]
values_dict = {'c': True, 'a': 4, 'b': 'опять строка'}
print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры:
values_list_2 = (5, 'строки они повсюду')
print_params(*values_list_2, 42)
