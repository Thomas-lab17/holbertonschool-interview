#!/usr/bin/python3
"""Read stdin line by line and print metrics every 10 lines.

Expected input format (otherwise the line is ignored):
<ip> - [<date>] "GET /projects/260 HTTP/1.1" <status_code> <file_size>

After every 10 lines and/or a keyboard interruption (CTRL+C), prints:
- File size: <total_size>
- <status_code>: <count> (ascending order)

The module is safe to import (no work is performed on import).
"""

import re
import sys


LOG_RE = re.compile(
    r'^(?P<ip>\S+) - '\
    r'\[(?P<date>[^\]]+)\] '\
    r'"GET /projects/260 HTTP/1\.1" '\
    r'(?P<status>\d+) (?P<size>\d+)$'
)

VALID_STATUS = {"200", "301", "400", "401", "403", "404", "405", "500"}


def _print_stats(total_size, status_counts):
    """Print the current aggregated metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(VALID_STATUS, key=int):
        count = status_counts.get(code, 0)
        if count:
            print("{}: {}".format(code, count))


def main():
    total_size = 0
    status_counts = {}
    line_count = 0
    last_print_at = 0

    try:
        for line in sys.stdin:
            line_count += 1
            line = line.rstrip("\n")

            match = LOG_RE.match(line)
            if match:
                status = match.group("status")
                size = match.group("size")

                try:
                    total_size += int(size)
                except (TypeError, ValueError):
                    pass

                if status in VALID_STATUS:
                    status_counts[status] = status_counts.get(status, 0) + 1

            if line_count % 10 == 0:
                _print_stats(total_size, status_counts)
                last_print_at = line_count

    except KeyboardInterrupt:
        _print_stats(total_size, status_counts)
        return

    if last_print_at != line_count or line_count == 0:
        _print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
