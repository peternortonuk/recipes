"""
The class hierarchy for built-in exceptions is:
https://docs.python.org/3/library/exceptions.html#exception-hierarchy

https://stackoverflow.com/questions/11551996/why-do-we-need-the-finally-clause-in-python
https://realpython.com/python-exceptions/
"""

x = input('enter a number...')
print(f'you entered: {x}\n')

try:
    print('\nconverting the input to a float')
    x = float(x)
    print('...worked fine')
except Exception as exc:
    print('...this didnt work')
    print(f'\nthis is the Exception message... {exc}\n\n')

try:
    print('\ndividing my number by the input')
    result = 10 / x
    print('...worked fine')
except Exception as exc:
    print('...this didnt work')
    print(f'this is the Exception message... {exc}\n\n')
    result = 0


print(f'\nbut whatever, everything is great, here is the result: {result}')
print('===============================')
pass
