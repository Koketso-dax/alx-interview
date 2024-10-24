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

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) >= 7:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print("{}: {}".format(code, status_codes[code]))
except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))
