
# ==============================================================================
# decorator with arguments
# need an extra nested function because first job is to return
# function without args


def decorator_with_args(arg1, arg2, arg3):

    def wrap(fn):
        print("Inside wrap()")  # executes when function is constructed

        def wrapper(*args):  # a1, a2, a3, a4
            print("Inside wrapped_f()")
            print("decorator_with_args arguments:", arg1, arg2, arg3)
            fn(*args)
            print("After f(*args)")
        return wrapper

    return wrap


@decorator_with_args("hello", "world", 42)
def say_hello(a1, a2, a3, a4):
    print('say_hello arguments:', a1, a2, a3, a4)


if __name__ == '__main__':

    print('===== decorator with arguments =====')
    say_hello("say", "hello", "argument", "list")