#!/usr/bin/python3
"""Prime Game module."""


def isWinner(x, nums):
    """Determine the winner of the prime game over x rounds.

    Args:
        x (int): number of rounds.
        nums (list): list of n values, one per round.

    Returns:
        Name of the player that won the most rounds, or None if tied.
    """
    if x <= 0 or nums is None or len(nums) == 0:
        return None

    max_n = max(nums)
    sieve = [True] * (max_n + 1)
    if max_n >= 0:
        sieve[0] = False
    if max_n >= 1:
        sieve[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    prime_count = [0] * (max_n + 1)
    count = 0
    for i in range(2, max_n + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count

    maria = 0
    ben = 0
    for n in nums:
        if n < 2:
            ben += 1
        elif prime_count[n] % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
