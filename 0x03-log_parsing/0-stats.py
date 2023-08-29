#!/usr/bin/python3
"""Log Parse"""
import sys
import collections
import signal


total_size = 0
status_counts = collections.defaultdict(int)
line_count = 0

def print_statistics():
    print(f"Fil file size: {total_size}")
    for status in sorted(status_counts):
        print(f"{status}: {status_counts[status]}")

def handle_interrupt(signum, frame):
    print_statistics()
    sys.exit(0)

# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) >= 7: 
            status_code = parts[-2]
            if status_code.isnumeric():
                status_code = int(status_code)
                if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    file_size = int(parts[-1])
                    total_size += file_size
                    status_counts[status_code] += 1
                    line_count += 1

        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    pass


print_statistics()

