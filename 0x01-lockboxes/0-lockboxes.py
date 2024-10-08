#!/usr/bin/python3
"""
    checkUnlockAll function module
    Returns True if all boxes can be opened returns False otherwise.
"""


def canUnlockAll(boxes: list) -> bool:
    """
    Returns True if all boxes can be opened else returns False.
    Args:
        boxes (list): list of lists of positive integers.
    ---
    Returns:
        bool: True if all boxes can be opened else returns False.
    ---
    Example:
        >>> canUnlockAll([[1], [2], [3], [4], []])
        True
        >>> canUnlockAll([[1, 4, 6], [2], [0, 4, 1],
                          [5, 6, 2], [3], [4, 1], [6]])
        True
        >>> canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]])
        False
    """
    if not boxes or type(boxes) is not list:
        return False
    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
