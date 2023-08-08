#!/usr/bin/env python3
""" Lock boxes searches for key
 """


def canUnlockAll(boxes):
    """_summary_

    Args:
        boxes (_type_): _description_

    Returns:
        _type_: _description_
    """
    unlocked_boxes = [False] * len(boxes)
    unlocked_boxes[0] = True
    keys_queue = [0]

    while keys_queue:
        current_box = keys_queue.pop()
        for key in boxes[current_box]:
            if not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                keys_queue.append(key)

    return all(unlocked_boxes)
