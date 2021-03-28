"""
https://docs.python.org/3/glossary.html#term-generator

generator function = function which returns a generator iterator... looks like a normal function except that it contains
yield expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with
the next() function.

generator iterator = object created by a generator function.


https://www.python.org/dev/peps/pep-0255/
PEP 255 -- Simple Generators
Abstract... the concept of generators to Python, as well as a new... yield statement.

A function that contains a yield statement is called a generator function.
Generator functions are a special kind of function that return a lazy iterator. 

Each time the next() method of a generator-iterator is invoked, the code in 
the body of the generator-function is executed until a yield statement is encountered.

If a yield statement is encountered, the state of the function is frozen, and the 
value of expression_list is returned to .next()'s caller. By "frozen" we mean that 
all local state is retained, including the current bindings of local variables, 
the instruction pointer, and the internal evaluation stack: enough information is saved 
so that the next time .next() is invoked, the function can proceed exactly 
as if the yield statement were just another external call.


https://www.python.org/dev/peps/pep-0289/
PEP 289 -- Generator Expressions
Abstract... a high performance, memory efficient generalization of list comprehensions and generators


https://realpython.com/introduction-to-python-generators/
When you call special methods on the generator iterator, such as next(), the code within the function is executed
up to yield.

https://pythontips.com/2013/09/29/the-python-yield-keyword-explained/

https://realpython.com/lessons/understanding-generators/

"""


print('\n=========================================================\n'
      'example: generator expression'
      '\n========\n')

g = (x**2 for x in range(10))
print(next(g))
print(next(g))
print(next(g))


# ===================================================================


print('\n=========================================================\n'
      'example: simple generator'
      '\n========\n')


def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


g = fib()
print(next(g))
print(next(g))
print(next(g))
pass

# ===================================================================
'''
https://realpython.com/introduction-to-python-generators/
'''
print('\n=========================================================\n'
      'example: generating an infinite sequence'
      '\n========\n')


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


gen = infinite_sequence()  # <generator object infinite_sequence at 0x0000013EE23A8C78>
print(next(gen))
print(next(gen))
print(next(gen))


print('\n=========================================================\n'
      'example: using StopIteration '
      '\n========\n')

letters = ["a", "b", "c", "y"]
it = iter(letters)
while True:
    try:
        letter = next(it)
    except StopIteration:
        break
    print(letter)

# ===================================================================
'''
When a return statement is encountered, control proceeds as in any function return, 
executing the appropriate finally clauses (if any exist). Then a StopIteration exception 
is raised, signalling that the iterator is exhausted. A StopIteration exception is 
also raised if control flows off the end of the generator without an explicit return.
'''
print('\n=========================================================\n'
      'example: multiple yield statements'
      '\n========\n')

chosencurves = ['NBP', 'TTF']
chosenvols = ['VOL_NBP', 'VOL_TTF']


def all_curves():
    for curve in chosencurves:
        yield curve
    for vol in chosenvols:
        yield vol


iter_curves = all_curves()
print(next(iter_curves))
print(next(iter_curves))
print(next(iter_curves))
print(next(iter_curves))


print('\n=========================================================\n'
      'example:'
      '\n========\n')


def cumsum(lst):
    result = 0
    iter_ = iter(lst)
    while True:
        result += next(iter_)
        yield result

print(cumsum([1,2,3]))

pass


'''
david beazley: iteration protocol and customisation via generators
saved to google drive
62-14.1
'''

print('\n=========================================================\n'
      'example: __iter__'
      '\n========\n')

names = ['YHOO', 'IBM', 'AAPL']
for name in names:
    print(name)

# under the hood its doing this...
it = names.__iter__()
print(next(it))
print(next(it))
print(next(it))
print(next(it))


# this is a generator function
def countdown(n):
    print('counting down from ', n)
    while n>0:
        yield n
        n -= 1
    print('done')


# this doesnt do anything except assign the generator function
y = countdown(5)
print(y)

# now the loop iterates through and each step runs the function
for x in y:
    print(x)


# related to a list comprehension
nums = [1, 2, 3, 4, 5, 6]
squares = [x**2 for x in nums]
print(squares)

# we have generator expressions
squares = (x**2 for x in nums)
print(squares)


# but they can't be re-used
# one way around this is...
class Countdown(object):
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        print('counting down from ', self.n)
        while self.n > 0:
            yield self.n
            self.n -= 1
        print('done')


c = Countdown(5)
for x in c:
    print(x)
