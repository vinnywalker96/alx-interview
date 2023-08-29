#!/usr/bin/python3
"""Log parsing"""

import sys

total_size = 0
counts = {}
try:
    line_count = 0
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        if len(parts) != 10:
            continue
        ip = parts[0]
        code = parts[8]
        file_size = int(parts[9])

        total_size += file_size

        if code.isdigit():
            code = int(code)
            if code in counts:
                counts[code] += 1
            else:
                counts[code] = 1
        line_count += 1

        if line_count % 10 == 0:
            print(f'File size: {total_size}')
            for status in sorted(counts.keys()):
                print(f'{status}: {counts[status]}')
except KeyboardInterrupt:
    print(f"Total file size: {total_size}")
    for status in sorted(counts.keys()):
        print(f"{status}: {counts[status]}")
