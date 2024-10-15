#!/usr/bin/python3
""" repeatedly dividing n by its smallest possible prime factor,
which corresponds to the minimum number of operations needed
to achieve that factor. """


def minOperations(n: int) -> int:
    """ Return min number of ops required to copy x paste. """
    if n <= 1:
        return 0

    ops:int = 0
    i: int = 2
    while i <= n:
        if n % i == 0:
            ops += i
            n /= i
        else:
            i += 1
    return ops
