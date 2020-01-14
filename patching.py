from functools import partial
import math


# ====================================
# generic monkey patching
def monkey(v):
    return math.log(v, 100)


math.log100a = monkey
print(math.log100a(10))

# ====================================
# patching with lambda
math.log100b = lambda v: math.log(v, 100)
print(math.log100b(10))


# ====================================
# failed attempt with partial
# when using positional arguments with partial, values are passed starting with the first one
# math.log doesnt accept kwargs, and base is the *second* argument
log100c = partial(math.log, 100)
print(log100c(10))


# ====================================
# now with a closure accessing 'base' from enclosing function
def monkey1(base):
    def monkey2(v):
        return math.log(v, base)
    return monkey2


math.log100d = monkey1(100)
print(math.log100d(10))
