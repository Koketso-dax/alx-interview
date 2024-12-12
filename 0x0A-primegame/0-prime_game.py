#!/usr/bin/python3
""" Module defining the isWinner function to
    determine the winner of a prime number game.
"""


def isWinner(x, nums):
    """
    Determine the winner of a prime number game played over multiple rounds.

    Parameters:
    x (int): The number of rounds to play.
    nums (list of int): A list where each element
    represents the maximum number for each round.

    Returns:
    str: The name of the player who won the most rounds, or None if drawn.
    """
    maria_wins = 0
    ben_wins = 0

    for num in nums[:x]:
        round_set = list(range(1, num + 1))
        primes_set = primes_in_range(1, num)

        if not primes_set:
            ben_wins += 1
            continue

        is_maria_turn = True

        while True:
            if not primes_set:
                if is_maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            smallest_prime = primes_set.pop(0)
            round_set.remove(smallest_prime)

            round_set = [x for x in round_set if x % smallest_prime != 0]

            is_maria_turn = not is_maria_turn

    if maria_wins > ben_wins:
        return "Winner: Maria"

    if maria_wins < ben_wins:
        return "Winner: Ben"

    return None


def is_prime(n):
    """
    Check if a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """
    Generate a list of prime numbers within a given range.

    Parameters:
    start (int): The starting number of the range (inclusive).
    end (int): The ending number of the range (inclusive).

    Returns:
    list of int: A list of prime numbers within the specified range.
    """
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    return primes
