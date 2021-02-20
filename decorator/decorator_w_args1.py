"""
decorator takes args
function doesnt

decorator calls function a given number of times

when decorator needs args then add an extra nested function because first job is to return
function without args
"""

args = (2, 3, 4, 5)


def my_decorator_with_args(args_):
    print('inside my_decorator\n')
    count, *args_ = args_  # just take the first value from the tuple

    def my_wrapper(f):
        def decorated():
            for i in range(count):
                print('before function is called')
                f()
                print('after function is called\n')
        return decorated
    return my_wrapper


# without sugar
def my_function1():
    print('...Wheee!')


# with sugar
@my_decorator_with_args(args)
def my_function2():
    print('...Whooo!')


# ==============================================================================
if __name__ == '__main__':

    # without sugar
    print('\n============================')
    print('function call WITHOUT sugar:\n')

    # returns my_wrapper
    wrapper = my_decorator_with_args(args)

    # my_wrapper is a function that accepts a function as an argument
    # and returns a new decorated function
    decorated_ = wrapper(my_function1)
    decorated_()

    # with sugar
    print('\n=========================')
    print('function call WITH sugar:\n')

    my_function2()





