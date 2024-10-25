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
if a status code doesnt appear or is not an integer, pass
format: <status code>: <number>
status codes are printed ascending order
"""
import signal
import sys
import re


def print_stats(log: dict) -> None:
    """
    helper function to display stats
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))


def signal_handler(sig, frame):
    print_stats(log)
    sys.exit(0)


if __name__ == "__main__":
    regex = re.compile(
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET \/projects\/260 HTTP\/1.1" (.{3}) (\d+)')  # nopep8

    line_count = 0
    log = {}
    log["file_size"] = 0
    log["code_frequency"] = {
        str(code): 0 for code in [
            200, 301, 400, 401, 403, 404, 405, 500]}

    signal.signal(signal.SIGINT, signal_handler)
    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if (match):
                line_count += 1
                code = match.group(1)
                file_size = int(match.group(2))

                # File size
                log["file_size"] += file_size

                # status code
                if (code.isnumeric()):
                    log["code_frequency"][code] += 1

                if (line_count % 10 == 0):
                    print_stats(log)
    finally:
        print_stats(log)
