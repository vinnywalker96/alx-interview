#!/usr/bin/python3
"""Lock boxes searches for key"""


def canUnlockAll(boxes):
    """_summary_

    Args:
        boxes (_type_): _description_

    Returns:
        _type_: _description_
    """
    num_boxes = len(boxes)
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < num_boxes:
                keys.append(new_key)
    return len(keys) == num_boxes
