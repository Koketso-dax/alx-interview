#!/usr/bin/python3
"""Given a pile of coins of different values, determine
the fewest number of coins needed to meet a given amount total."""
import sys


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
    if total != 0:
        return -1
    return count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: n <coins>")
        sys.exit(1)
    try:
        coins = [1, 2, 25]
        n = int(sys.argv[1])
        print(makeChange(coins, n))
    except ValueError:
        print("Error")
