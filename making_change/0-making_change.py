#!/usr/bin/python3
"""Making Change module."""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet a total.

    Args:
        coins (list): values of the coins available.
        total (int): amount to meet.

    Returns:
        Fewest number of coins needed to meet total, 0 if total is 0
        or less, or -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    dp = [0] + [total + 1] * total
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1

    return dp[total] if dp[total] <= total else -1
