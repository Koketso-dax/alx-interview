#!/usr/bin/python3
""" Solution to the N-Queens Problem. Given an input N which is
    the size of a board (N x N), determine
"""
import sys


def n_queens(n):
    """ Solves the N-Queens problem. """
    if n == 2 or n == 3:
        print("N = {} does not have any possible solutions".format(n))
        return

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, solutions)
    for solution in solutions:
        for row in solution:
            print(row)
        print()


def solve_n_queens(board, row, solutions):
    """ Solves the N-Queens problem. """
    if row == len(board):
        solutions.append([row[:] for row in board])
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_n_queens(board, row + 1, solutions)
            board[row][col] = 0


def is_safe(board, row, col):
    """ Checks if a queen can be placed on the board. """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    n_queens(n)
