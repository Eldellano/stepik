a = int(input())
b = int(input())

n = 1 #число на которое делим (кусочки)
while ((n % a) != 0) or ((n % b) != 0):
    n += 1
print(n)
