p=0
l=[]
tem=0


for _ in range(4):
    o, i = map(int, input().split())
    p=-o+i
    l.append(tem+p)
    tem += p

result=max(l)
print(result)