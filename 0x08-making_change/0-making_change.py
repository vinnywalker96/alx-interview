#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """Calculate Change"""
    if total < 0:
        return -1
    res = [float('inf')] * (total + 1)
    res[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            if res[i - coin] != float('inf'):
                res[i] = min(res[i], res[i - coin] + 1)
    if res[total] == float('inf'):
        return -1
    return res[total]
