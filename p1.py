import sys
from sys import stdin

try:
    for line in stdin:
        result  = ""
        for c in line:
            if c.isalpha():
                result += c
        print(result.upper())
except EOFError:
    sys.exit(0)
