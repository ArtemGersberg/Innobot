def function_father(x) -> callable:
    def inside_function(repeat: int):
        print(x * repeat)

    return inside_function


first = function_father("hello")
second = function_father("world")


# first(1)
# second(2)
# first(3)

def double(func):
    def wrapper(a, b):
        return func(a, b) * 2

    return wrapper


@double  # sum = double(sum)
def sum(a, b):
    return a + b


@double
def mut(a, b):
    return a * b


@double
def sub(a, b):
    return a - b


print(mut(2, 3))
