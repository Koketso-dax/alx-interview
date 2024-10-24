#!/usr/bin/python3
""" This script reads stdin line by line and computes these metrics:
input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
if the format is incorrect, the line is skipped.
After every 10 lines and/or a keyboard interruption (CTRL + C)
The following is printed:
File size: <total size>
<total size> is the aggregate of <file size>
Number of lines by status code:
possible status code: [200, 301, 400, 401, 403, 404, 405, 500]
if a status code doesn’t appear or is not an integer, pass
format: <status code>: <number>
status codes are printed ascending order
"""
import sys


def print_stats(total_size, status_codes):
    """Print accumulated statistics."""
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    total_size = 0
    line_count = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                parts = line.split()
                if len(parts) < 7:
                    continue

                # Get status code and file size from the end
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                # Update statistics
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += file_size

            except (ValueError, IndexError):
                continue
            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # Print final stats on CTRL+C
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
