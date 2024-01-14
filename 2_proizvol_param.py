def test(a, b, c, *args, **kwargs):
    print(a, b, c, args, kwargs)


test(1, 2, 3, 4, 5, 6, семь=7)


def factorial(n):
    if n == 1:
        return 1
    factorial_n_minus_1 = factorial(n=n-1)
    return n*factorial_n_minus_1


print(factorial(10))
