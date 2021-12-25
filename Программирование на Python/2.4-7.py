a = input()
n = len(a) - 1
i = 0
cnt = 0

while i <= n:
    if i == n:
        if a[i] == a[i]:
            # i += 1
            cnt += 1
            print(a[i] + str(cnt), end='')
            break
        elif a[i] != a[i]:
            cnt += 1
            print(a[i] + str(cnt), end='')
            i += 1
            cnt = 0
            continue

    if a[i] == a[i + 1]:
        i += 1
        cnt += 1
    elif a[i] != a[i + 1]:
        cnt += 1
        print(a[i] + str(cnt), end='')
        i += 1
        cnt = 0
        