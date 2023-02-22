n1=int(input())
n2=int(input())
n3=list(map(int,input().split()))
print(n3)
r=0

for case in range(1, n1+1):
    if len(n3)==n2:
        for n in n3:
            r += n

print(r)
