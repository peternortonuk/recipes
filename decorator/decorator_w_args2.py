"""
function takes args
decorator doesnt

decorator calls function twice
"""

text1 = '...Wheee!'
text2 = '...Whooo!'


def my_decorator(f):
    print('inside my_decorator\n')

    def decorated(*args, **kwargs):
        f(*args, **kwargs)
        f(*args, **kwargs)
    return decorated


# without sugar
def my_function1(text):
    print(text)


# with sugar
@my_decorator
def my_function2(text):
    print(text)


# ==============================================================================
if __name__ == '__main__':

    # without sugar
    print('\n============================')
    print('function call WITHOUT sugar:\n')

    decorated_ = my_decorator(my_function1)
    decorated_(text1)

    # with sugar
    print('\n=========================')
    print('function call WITH sugar:\n')

    my_function2(text2)
