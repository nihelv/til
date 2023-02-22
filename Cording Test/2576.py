result=[]

for n in range(7):
    a=int(input())
    if a % 2 == 1:
        result.append(a)

if len(result)==0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
