import sys
import re

pattern = r'\b((\w)(\w))'
for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(pattern, r'\3\2', line)
    print(line)