N, X = map(int, input().split())
A=list(map(int, input().split()))
A_1=[]

for n in A:
    if 1<=n and n<X:
        A_1.append(n)

print(*A_1)