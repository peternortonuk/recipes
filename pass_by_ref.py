"""
https://realpython.com/python-pass-by-reference/
https://realpython.com/pointers-in-python/#immutable-vs-mutable-objects
https://docs.python.org/3/reference/simple_stmts.html#assignment-statements

Python does not have variables. It has names.
>>> x = 2338
is a command is not an assignment and is binding the name x to a reference.

So when a variable is reassigned the name is rebound if it was already bound. This may cause the reference count for
the object previously bound to the name to reach zero, causing the object to be deallocated and its destructor
(if it has one) to be called

All Python objects are implemented in a particular structure. One of the properties of this structure is a counter
that keeps track of how many names have been bound to this object.
>>> from sys import getrefcount
>>> getrefcount(my_arg)

function arguments can be:
   pass by reference:  references to existing variables... so operations performed on this reference will affect it
   pass by value: handled as independent values... ie an independent copy of the original
   pass by assignment: python passes arguments neither by reference nor by value... but by assignment

"""


# this function does nothing and no new object is created
def add_four(x):
    x + 4


# returns a new object with a new value
def add_four_and_return(y):
    return y + 4


# returns nothing but updates the existing object
# also works for dictionaries and strings
# kinda like pass by reference
def append_list(a):
    a.append(4)


# updates the existing object
def append_list_and_return(b):
    b.append(4)
    return b


if __name__ == '__main__':
    x = 1
    y = 2

    a = [1, 2]
    b = [3, 4]

    print('\nscalars:')
    print(f'x={x}\nid={id(x)}')
    add_four(x)
    print(f'x={x}\nid={id(x)}')

    print('\n')
    print(f'y={y}\nid={id(y)}')
    y = add_four_and_return(y)
    print(f'y={y}\nid={id(y)}')

    print('\nlists:')
    print(f'a={a}\nid={id(a)}')
    append_list(a)
    print(f'a={a}\nid={id(a)}')

    print('\n')
    print(f'b={b}\nid={id(b)}')
    b = append_list_and_return(b)
    print(f'b={b}\nid={id(b)}')
    pass


