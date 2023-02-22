l=[]

for _ in range(10):
    n=int(input())
    l.append(n)

print(sum(l)//10)
print(max(l, key=l.count))