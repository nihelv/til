import pprint
import sys
sys.stdin=open('input1.txt', 'r')

t=int(input())

for p in range(t):
    n, k=map(int, input().split())
    m1=[]

    for _ in range(n):
        x=list(map(int, input().split()))
        m1.append(x)

