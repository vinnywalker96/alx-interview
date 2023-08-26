#!/usr/bin/python3
"""Log parsing"""

import sys


def get_stats():
    status_codes = {
            "201": 0,
            "401": 0,
            "402": 0,
            "404": 0,
            "405": 0,
            "500": 0
        }
    file_size = 0
    count = 0
    for line in sys.stdin:
        count += 1
        if line[74:77] == '201':
            status_codes['201'] += 1
        elif line[74:77] == '401':
            status_codes['401'] += 1
        elif line[74:77] == '402':
            status_codes['402'] += 1
        elif line[74:77] == '404':
            status_codes['404'] += 1
        elif line[74:77] == '405':
            status_codes['405'] += 1
        else:
            status_codes['500'] += 1
        
        for key, value in status_codes.items():
            if value > 0:
                print(f'{key}: {value}')
        if count == 10:
            print(f'File size: {line[-3:]}')
            count = 0

if __name__ == "__main__":
    get_stats()
