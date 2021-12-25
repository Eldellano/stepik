n = int(input())
coord_1 = 0
coord_2 = 0

for i in range(n):
    direct = [str(i) for i in input().split()]
    if direct[0] == 'север':
        coord_2 += int(direct[1])
    elif direct[0] == 'юг':
        coord_2 -= int(direct[1])
    elif direct[0] == 'восток':
        coord_1 += int(direct[1])
    elif direct[0] == 'запад':
        coord_1 -= int(direct[1])

print(coord_1, coord_2)
