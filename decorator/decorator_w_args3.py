"""
decorator takes args
and function takes args

"""

args = (5, 3, 4, 5)

text1 = '...Wheee!'
text2 = '...Whooo!'


def my_decorator_with_args(decorator_args):
    print('inside my_decorator\n')
    count, *args_ = decorator_args  # just take the first value from the tuple

    def my_wrapper(f):
        def decorated(*func_args):
            for i in range(count):
                print('before function is called')
                f(func_args)
                print('after function is called\n')
        return decorated
    return my_wrapper


# without sugar
def my_function1(text):
    print(text)


# with sugar
@my_decorator_with_args(args)
def my_function2(text):
    print(text)


# ==============================================================================
if __name__ == '__main__':

    # without sugar
    print('\n============================')
    print('function call WITHOUT sugar:\n')

    wrapper_ = my_decorator_with_args(args)
    decorated_ = wrapper_(my_function1)
    decorated_(text1)

    # with sugar
    print('\n=========================')
    print('function call WITH sugar:\n')

    my_function2(text2)
    pass
