import sys
j = 0
for i in sys.argv:
    if j != len(sys.argv) - 1:
        print(sys.argv[j + 1], end = ' ')
        j += 1
