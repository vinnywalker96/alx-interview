#!/usr/bin/env python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Check if
    utf-8
    """
    min_val = 0
    max_val = 127
    for val in data:
        if not (min_val <= val <= max_val):
            return False
    return True
