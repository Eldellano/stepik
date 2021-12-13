import sys
import re

match = r'cat'
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(match, line)) >= 2:
        print(line)
