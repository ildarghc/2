from dis import dis


def some_func(param):
    a = 42
    print(a, param)
    return a


dis(some_func)
