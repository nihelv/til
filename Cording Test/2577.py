m=[]
# m=[150, 266, 427]

for i in range(1, 4):
    a=int(input())
    m.append(a)

n_temp=m[0]*m[1]*m[2]
n=str(n_temp)

for k in range(10):
    l=n.count(str(k))
    print(l)
