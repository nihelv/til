n = int(input())
s = 0
r = 0
k = list(map(int, input().split()))

for i in range(n):
    if k[i] == 1:
        s += 1
        r += s
    else:
        s = 0