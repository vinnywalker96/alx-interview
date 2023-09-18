#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(n):
    '''calculates the fewest number of
    operations needed 
    '''
    pasted_chars = 1  # how many chars in the file
    clipboard = 0  # how many H's copied
    counter = 0  # operations counter

    while pasted_chars < n:
        # if did not copy anything yet
        if clipboard == 0:
            # copyall
            clipboard = pasted_chars
            # increment operations counter
            counter += 1

        # if haven't pasted anything yet
        if pasted_chars == 1:
            # paste
            pasted_chars += clipboard
            # increment operations counter
            counter += 1
            continue

        remaining = n - pasted_chars  
        if remaining < clipboard:
            return 0

        # if can't be devided
        if remaining % pasted_chars != 0:
            # paste current clipboard
            pasted_chars += clipboard
            # increment operations counter
            counter += 1
        else:
            # copyall
            clipboard = pasted_chars
            # paste
            pasted_chars += clipboard
            # increment operations counter
            counter += 2

    # if got the desired result
    if pasted_chars == n:
        return counter
    else:
        return 0
