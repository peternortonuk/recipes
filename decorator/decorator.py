"""
a decorator function accepts a function as an argument and returns a modified function

without syntactic sugar, we pass our function to the decorator and get an
enhanced function returned back; we can then run this new function

with syntactic sugar, we run in one line

remember, this is it:
    f1 = my_decorator(just_some_function1)
    f1()

https://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html#using-functions-as-decorators
https://realpython.com/primer-on-python-decorators

"""

print('\n====================================')
print('start here; define some functions:\n')


def my_decorator(f):
    print('inside my_decorator\n')

    def decorated():
        print('before function is called')
        f()
        print('after function is called\n')

    return decorated


def my_function1():
    print('...Wheee!')


@my_decorator
def my_function2():
    print('...Whooo!')


if __name__ == '__main__':

    # without sugar
    print('\n============================')
    print('function call WITHOUT sugar:\n')

    decorated_ = my_decorator(my_function1)
    decorated_()
    
    # with sugar
    print('\n=========================')
    print('function call WITH sugar:\n')

    my_function2()
    pass
