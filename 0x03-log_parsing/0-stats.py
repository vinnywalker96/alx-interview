#!/usr/bin/python3
"""Log parsing"""

import sys
import collections


def log_stats():
    total_size = 0
    status_counts = collections.defaultdict(int)

    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 10 and parts[8].isnumeric():
            id = parts[0]
            date = parts[2][1:-1]
            request = " ".join(parts[5:8])
            status_code = int(parts[8])
            file_size = int(parts[9])

            if status_code.isdigit():
                total_size += int(file_size)
                status_counts[int(status_code)] += 1
        
            if len(status_counts) % 10 == 0:
                print(f"File Size: {total_size}")
                for status_code, count in sorted(status_counts.items()):
                    print(f'{status_code}: {count}')


if __name__ == "__main__":
    log_stats()
