import sys

sys.stdin = open('input.txt', 'r')

cn=int(input()) #정점 갯수
nd=int(input()) #간선 갯수
v = [[]  for _ in range(cn+1)] #그래프 초기화

for i in range(nd): #
    c1, c2 = map(int, input().split())
    v[c1].append(c2)
    v[c2].append(c1)


