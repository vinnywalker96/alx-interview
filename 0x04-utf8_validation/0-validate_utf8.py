#!/usr/bin/python3
"""UTF-8 Validation"""
from typing import Union


def validUTF8(data: Union[int, str]) -> bool:
    """Checks if utf8

    Args:
        data:(int / str)
    """
    min_val: int = 0
    max_val: int = 127
    for val in data:
        if not (min_val <= val <= max_val):
            return False
        else:
            chr(val)
            return True
