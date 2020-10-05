import itertools

very_nested_list = ['a', 'b', 'c', ['d', 'e'], ['f', ['g', 'h']], [[['i']]]]
slightly_nested_list = ['a', 'b', 'c', ['d', 'e']]

x = itertools.chain.from_iterable(very_nested_list)
# print(list(x))


def walk(iterable):
    if len(iterable) <= 1:
        return iterable
    else:
        element = iterable[0]
        return [element] + walk(iterable[1:])

print(walk(very_nested_list))
