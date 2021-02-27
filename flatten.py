import itertools

very_nested_list = ['a', 'bc', 3, ['d', 'e'], ['f', ['g', 'h']], [[['i']]]]
short_nested_list = [[[4]]]

# this is utter rubbish
# it cant deal with integers
# it cant deal with greater than one level of nesting
x = itertools.chain.from_iterable(very_nested_list)


def flatten(iterable):
    # these are the base cases
    if not isinstance(iterable, list):
        # if its not a list then return a list with a single entry
        return [iterable]
    elif isinstance(iterable, list) and len(iterable) == 1 and not isinstance(iterable[0], list):
        # if its a list with a single entry that isnt itself a list
        return iterable
    elif not iterable:
        # it could be an empty list
        return []
    # this is the recursive case
    else:
        return flatten(iterable[0]) + flatten(iterable[1:])


assert flatten(very_nested_list) == ['a', 'bc', 3, 'd', 'e', 'f', 'g', 'h', 'i']
assert flatten(short_nested_list) == [4]

print(very_nested_list)
print(flatten(very_nested_list))
