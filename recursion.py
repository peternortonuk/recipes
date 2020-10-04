from functools import lru_cache
num_of_terms = 10

print('\n=========================================================\n'
      'factorial'
      '\n========\n')

"""
https://realpython.com/lessons/defining-recursive-function/

5! = 5 * 4 * 3 * 2 * 1
5! = 5 * 4!  # look the function is on both sides; but on the right is a smaller version

factorial(5)
return 5 * factorial(4)
           return 4 * factorial(3)
                      return 3 * factorial(2)
                                 return 2 * factorial(1)
                                            return 1  # base case or stopping condition
                                 return 2 * 1 = 2
                      return 3 * 2 = 6
           return 4 * 6 = 24
return 5 * 24 = 120
"""


def factorial(n):
    print(n)
    # base case; the simplest version of the problem
    if n <= 1:
        return 1
    # recursive case
    else:
        return n * factorial(n - 1)


result = factorial(num_of_terms)
print(f'\nresult={result}')


print('\n=========================================================\n'
      'fibonacci'
      '\n========\n')

"""
https://realpython.com/lessons/fibonacci-and-optimizations/
"""


def fibonacci(n):
    print(n)
    # base cases; there are two here
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


result = fibonacci(num_of_terms)
print(f'\nresult={result}')


print('\n=========================================================\n'
      'fibonacci with caching'
      '\n========\n')

"""
https://realpython.com/lessons/fibonacci-and-optimizations/

there's a huge number of repeated calls in the previous example
so use caching to save the result of previous calls
"""


@lru_cache(maxsize=None)
def fibonacci_optimised(n):
    print(n)
    # base cases; there are two here
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # recursive case
    else:
        return fibonacci_optimised(n - 1) + fibonacci_optimised(n - 2)


result = fibonacci_optimised(num_of_terms)
print(f'\nresult={result}')

