#!/usr/bin/python3
"""Minimum Operations.

Given a single character ``H`` and only the operations ``Copy All`` and
``Paste``, determine the minimum number of operations needed to reach exactly
``n`` characters.
"""


def minOperations(n):
    """Return the fewest operations needed to reach ``n`` characters.

    The optimal strategy is to break ``n`` into its prime factors and sum
    those factors. Each factor represents one ``Copy All`` followed by the
    required number of ``Paste`` operations.

    Args:
        n (int): Target number of ``H`` characters.

    Returns:
        int: Minimum number of operations, or ``0`` if ``n`` is impossible.
    """
    if not isinstance(n, int) or n < 2:
        return 0

    operations = 0
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    if n > 1:
        operations += n

    return operations
