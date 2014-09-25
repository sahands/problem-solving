from functools import wraps


def make_dual(relation):
    @wraps(relation, ['__name__', '__doc__'])
    def dual(x, y):
        return relation(y, x)
    return dual


def dualordering(cls):
    """Class decorator that reverses all the orderings"""
    for func in ['__lt__', '__gt__', '__ge__', '__le__']:
        if hasattr(cls, func):
            setattr(cls, func, make_dual(getattr(cls, func)))

    return cls


if __name__ == "__main__":
    @dualordering
    class rs(str):
        pass

    x = rs("1")
    y = rs("2")

    print x < y
    print x <= y
    print x > y
    print x >= y
