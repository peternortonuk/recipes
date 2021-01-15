


x = input('enter a number...')
print(f'you entered: {x}\n')

try:
    print('\nconverting the input to a float')
    x = float(x)
    print('...worked fine')

    print('\ndividing my number by the input')
    result = 10 / x
    print('...worked fine\n')
except ZeroDivisionError as exc:
    print(f'this is the Exception type: {exc.__class__.__name__}')
    print(f'this is the Exception message: {exc.args}')
    result = 'puke'
except ValueError as exc:
    print(f'this is the Exception type: {exc.__class__.__name__}')
    print(f'this is the Exception message: {exc.args}')
    result = 'urg'
except Exception as exc:
    print(f'this is the Exception type: {exc.__class__.__name__}')
    print(f'this is the Exception message: {exc.args}')
    result = 'yuk'

print(f'\nbut whatever, everything is great, here is the result: {result}')
print('===============================')
pass
