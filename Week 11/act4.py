import doctest

"""
This is the "example" module.

It demonstrates the use of doctest for automatic testing using examples
written inside docstrings.

>>> factorial(5)
120
"""

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    This function includes doctests for validation.

    >>> [factorial(n) for n in range(6)]     # list of first 6 factorials
    [1, 1, 2, 6, 24, 120]
    >>> factorial(34)                        # factorial of 34
    295232799039604140847618609643520000000
    >>> factorial(-1)                        # negative input raises error
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    >>> factorial(30.1)                      # non-integer float raises error
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)                      # exact integer float works
    265252859812191058636308480000000

    >>> factorial(1e100)                     # extremely large number error
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    n = int(n) 
    if n + 1 == n:
        raise OverflowError("n too large")

    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    doctest.testmod()  # runs all examples in docstrings as tests
