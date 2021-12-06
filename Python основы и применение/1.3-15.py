n, k = map(int, input().split())
def res(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return res(n - 1, k) + res(n - 1, k - 1)
print(res(n, k))
