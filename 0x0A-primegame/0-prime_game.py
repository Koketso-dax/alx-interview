#!/usr/bin/python3
"""Prime game func"""


def isWinner(x, nums):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def get_primes(n):
        return [i for i in range(2, n + 1) if is_prime(i)]

    def play_game(n):
        primes = get_primes(n)
        turn = 0
        while primes:
            prime = primes.pop(0)
            primes = [p for p in primes if p % prime != 0]
            turn = 1 - turn
        return "Maria" if turn == 0 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for i in range(min(x, len(nums))):
        n = nums[i]
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
