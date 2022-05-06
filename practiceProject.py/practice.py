def fac(n):
    if n == 1:
        return n
    return n * fac(n - 1)


print(fac(5))


def zero_check(any_function):
    def inner_function(x, y):
        if y == 0:
            return "Y is zero"
        return any_function(x, y)

    return inner_function

@zero_check
def add(x, y):
    return (x + y)


print(add(x, y))
