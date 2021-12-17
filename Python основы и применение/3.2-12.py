import sys
import re

match = r'human'
for line in sys.stdin:
    line = line.rstrip()
    dupl = re.sub(match, 'computer', line)
    print(dupl)