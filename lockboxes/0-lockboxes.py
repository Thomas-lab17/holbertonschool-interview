#!/usr/bin/python3
"""Lockboxes

Given a list of boxes, each containing keys to other boxes, determine whether
all boxes can be opened starting from box 0.
"""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened.

    Args:
        boxes (list[list[int]]): boxes[i] contains keys found in box i.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not isinstance(boxes, list):
        return False

    n_boxes = len(boxes)
    if n_boxes == 0:
        return True

    opened = set([0])
    keys_to_process = [0]

    while keys_to_process:
        box_index = keys_to_process.pop()
        for key in boxes[box_index]:
            if (
                isinstance(key, int)
                and 0 <= key < n_boxes
                and key not in opened
            ):
                opened.add(key)
                keys_to_process.append(key)

    return len(opened) == n_boxes
