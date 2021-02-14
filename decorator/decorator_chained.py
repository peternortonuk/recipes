# ==============================================================================
# chained decorator


def makebold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"
    return wrapper


def makeitalic(fn):
    def wrapper():
        return "<i>" + fn() + "</i>"
    return wrapper


@makebold
@makeitalic
def hello():
    return "hello world"


# ==============================================================================
if __name__ == '__main__':

    print(hello())
