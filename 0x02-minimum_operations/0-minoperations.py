#!/usr/bin/python3
"""Minimal Operation"""


def minOperations(n: int) -> int:
    """Calculate possible operations

    Args:
        n (int)
    """
    clipboard = ""
    current_string = "H"
    count = 0
    while len(current_string) < n:
        if (n - len(current_string)) % len(current_string) == 0:
            clipboard = current_string
            count += 1
        current_string += clipboard
        count += 1
    return count
