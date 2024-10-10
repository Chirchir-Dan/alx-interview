#!/usr/bin/env python3
"""
Module to determine if all boxes can be unlocked.

This module contains a function, `canUnlockAll`, which checks if all 
locked boxes can be opened given the keys inside each box. The first box 
is assumed to be unlocked at the start.

Function:
    canUnlockAll(boxes): Returns True if all boxes can be opened, 
                         otherwise returns False.
"""

def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Each box is represented as a list of keys, where a key with the same 
    number as a box opens that box.

    Parameters:
    boxes (list of list): A list of lists where each sublist contains 
                          the keys that can unlock other boxes.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    unlocked = [False] * len(boxes)  # Track which boxes are unlocked
    unlocked[0] = True  # The first box is unlocked
    queue = [0]  # Initialize queue with the first box index

    while queue:
        current_box = queue.pop(0)  # Get the next box to unlock
        for key in boxes[current_box]:  # Iterate over the keys in the current box
            if key < len(boxes) and not unlocked[key]:  # Validate key
                unlocked[key] = True  # Mark the box as unlocked
                queue.append(key)  # Add the unlocked box to the queue

    return all(unlocked)  # Check if all boxes are unlocked
