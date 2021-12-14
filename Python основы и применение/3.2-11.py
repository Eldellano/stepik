import sys
import re

match = r'\b(\w+)\1\b'
for line in sys.stdin:
    line = line.rstrip()
    if re.search(match, line):
        print(line)