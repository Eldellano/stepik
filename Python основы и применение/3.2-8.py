import sys
import re

match = r'\bcat\b'
for line in sys.stdin:
    line = line.rstrip()
    if re.search(match, line):
        print(line)
