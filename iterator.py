"""
https://docs.python.org/3/glossary.html#term-iterator

An object representing a stream of data. Repeated calls to the iterator’s __next__() method (or passing it to the
built-in function next()) return successive items in the stream. When no more data are available a StopIteration
exception is raised instead. Iterators are required to have an __iter__() method that returns the iterator object itself


https://dbader.org/blog/python-iterators

Python’s iterator protocol: Objects that support the __iter__ and __next__ dunder methods
automatically work with for-in loops.

Iterators provide a sequence interface to Python objects that’s memory efficient and considered Pythonic.

Class-based iterators are only one way to write iterable objects in Python.

In this example: Repeater and RepeaterIterator are working together to support Python’s iterator protocol.
The two dunder methods we defined, __iter__ and __next__, are the key to making a Python object iterable.
"""


class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


# under the hood
repeater = Repeater('Hello')
iterator = repeater.__iter__()
while True:
    item = iterator.__next__()
    print(item)

# alternatively
repeater = Repeater('Hello')
iterator = iter(repeater)
while False:
    item = next(iterator)
    print(item)

# for-in construct
for item in repeater:
    print(item)

