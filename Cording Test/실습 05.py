T=int(input())
s=0
r=0

for t in range(1, T + 1):
    v=int(input())
    if v == 0:
        r += 1
    elif v == 1:
        s += 1
        
if r > s:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")