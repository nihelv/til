n=int(input())
m=[]

for e in range(1, n+1):
    if n % e == 0:
        m.append(e)

print(*sorted(m))