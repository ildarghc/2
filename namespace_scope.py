def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()
# inner_function()

# вызов inner_function напрямую минуя функцию test_function приводит к ошибке is not defined,
# т.к. inner_function не объявлена в глобал и находится в локал test_function
