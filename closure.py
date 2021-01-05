"""
http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
https://gist.github.com/DmitrySoshnikov/700292
"""


def outer():
    x = 1
    def inner():
        print(x)
    return inner


foo = outer()
print(foo.__closure__[0].cell_contents)
pass
