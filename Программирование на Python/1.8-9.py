x = int(input())
y = int(input())
z = int(input())

_time = y * 60 + z
_time2 = _time + x

_time = (_time2 / 60)
_time3 = (_time2 % 60)

print(int(_time))
print(int(_time3))
