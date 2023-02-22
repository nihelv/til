import sys

sys.stdin = open("input.txt", "r")

m=int(input())

tem={
    1:1, 2:'*', 3:'**'
}


for i in range(m):
    x, y = map(int, input().split())
    if tem[x] == 1:
        tem[y] = tem[x]
        tem[x] = '***'
    else:
        tem[x] = tem[y]
        tem[y] = '***'
            
for e in [1, 2, 3]:
    if tem[e] == 1:
        print(e)
        break