"""
Число делится на 3 тогда и только тогда, когда сумма его цифр стоящих на четных местах отличается от суммы цифр,
стоящих на нечетных местах, на число, делящееся на 3
"""

import sys
import re

pattern = r'(1|0){1,}'


def binary_check(line):
    if ' ' not in line:
        cnt = 0
        sum_even, sum_odd = 0, 0
        for i in line:
            if cnt % 2 == 0:  # четный символ
                sum_even += int(i)
            else:  # нечетный символ
                sum_odd += int(i)
            cnt += 1
        if (sum_odd - sum_even) % 3 == 0:
            print(line)


for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line) is not None:
        binary_check(line)
