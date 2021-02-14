"""
a decorator function accepts a function as an argument and returns a modified function

without syntactic sugar, we pass our function to the decorator and get an
enhanced function returned back; we can then run this new function

with syntactic sugar, we run in one line

remember, this is it:
    f1 = my_decorator(just_some_function1)
    f1()
"""


def my_decorator(fn):
    print('inside decorator\n')

    def wrapper():
        print('inside wrapper')
        print('before function is called\n')
        fn()
        print('after function is called\n')

    return wrapper


# without sugar
def just_some_function1():
    print('Wheee!')


# with sugar
@my_decorator
def just_some_function2():
    print('Whooo!')


if __name__ == '__main__':

    # without sugar
    print('\n====================================')
    print('first function call (without sugar):\n')
    f1 = my_decorator(just_some_function1)
    f1()
    
    # with sugar
    print('\n=================================')
    print('first function call (with sugar):\n')
    just_some_function2()
    pass
