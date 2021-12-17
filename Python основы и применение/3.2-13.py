import sys
import re

match = r'a+\b'
for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(match, 'argh', line, 1, re.IGNORECASE)
    print(line)