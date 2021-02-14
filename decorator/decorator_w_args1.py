def my_decorator_with_args(*args):
    return my_decorator


# with args
@my_decorator_with_args(1, 2)
def just_some_function3():
    print("Whaaa!")


# ==============================================================================
if __name__ == '__main__':

    print(just_some_function3())