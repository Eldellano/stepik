import sys
import re

match = r'\\'
for line in sys.stdin:
    line = line.rstrip()
    if re.search(match, line):
        print(line)
