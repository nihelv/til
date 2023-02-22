#블랙잭

a, b = map(int, input().split())
m=list(map(int, input().split()))
tem=[]

for _ in range(a):
    for i in range(_+1, a):
        for e in range(i+1, a):
            s=m[_]+m[i]+m[e]
            if s <= b:
                tem.append(s)

print(max(tem))