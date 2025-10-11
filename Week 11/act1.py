def add(x, y):
    """
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return x + y


def multiply(x, y):
    """
    >>> multiply(5, 3)
    15
    >>> multiply(-7, 2)
    -14
    """
    return x * y


if __name__ == "__main__":
    import doctest
    doctest.testmod()
