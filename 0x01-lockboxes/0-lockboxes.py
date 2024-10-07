#!/usr/bin/python3
"""
    checkUnlockAll func module
    Returns True if all boxes can be opened, else False
"""


def canUnlockAll(boxes):
    """
    Returns True if all boxes can be opened, else False
    # Check if the input is a list
    if not isinstance(boxes, list):
        return False
    # Check if the list is empty
    if not boxes:
        return False
    # Check if the first box is empty
    """
    if not boxes:
        return False

    # Initialize a set to keep track of opened boxes
    opened_boxes = set()
    opened_boxes.add(0)  # Start with the first box

    # Iterate through the boxes
    for i in range(len(boxes)):
        # Check if the current box is opened
        if i in opened_boxes:
            # Add the keys in the current box to the set of opened boxes
            for key in boxes[i]:
                opened_boxes.add(key)

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)
