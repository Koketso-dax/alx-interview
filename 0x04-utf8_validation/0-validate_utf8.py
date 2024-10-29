#!/usr/bin/python3
"""UTF-8 validation module."""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints."""
    n = len(data)
    i = 0

    while i < n:
        if not isinstance(data[i], int) or data[i] < 0 or data[i] > 0x10ffff:
            return False

        if data[i] <= 0x7f:
            i += 1
        elif data[i] & 0b11110000 == 0b11100000:
            if i + 2 < n and all(data[i + j] &
                                 0xc0 == 0x80 for j in range(1, 3)):
                i += 3
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            if i + 1 < n and data[i + 1] & 0b11000000 == 0b10000000:
                i += 2
            else:
                return False
        elif data[i] & 0b11111000 == 0b11110000:
            if i + 3 < n and all(data[i + j] &
                                 0xc0 == 0x80 for j in range(1, 4)):
                i += 4
            else:
                return False
        else:
            return False

    return True
