import sys
sys.stdin=open('input.txt', 'r')

# N=int(input())

# s=0
# l=[]

# for _ in range(N):
#     x, y = map(int, input().split())
#     l.append(x + y)

# l1=list(reversed(sorted(l)))

# for i in l:
#     if i == l1[0] :
#         print(1, end=' ')

#     elif l1[1]-10 <= i <= l1[1]+10 :
#         print(2, end=' ')

#     elif l1[2]-10 <= i <= l1[2]+10 :
#         print(3, end=' ')

#     elif l1[3]-10 <= i <= l1[3]+10 :
#         print(4, end=' ')
    
#     else:
#         print(5, end=' ')

# 답은 나오는데 틀렸다고 함.
# 문제에 x, y의 합을 오차값 끼고 비교하는게 아니고
# x는 x끼리 y는 y끼리 비교하라고 써 있는데 꼼수부리지 맙시다


n = int(input())                             #케이스 수
l = []                                       #임보

for _ in range(n):                           #케이스 수 동안
    x, y = map(int, input().split())         #x, y를 입력받아서
    l.append((x, y))                         #x, y로 구성된 튜플을 리스트에 넣는다

for i in l:                                  #강제로 모든 경우의 수를 끌어낸다
    rank = 1                                 #if문이 전부 False라면 rank1(제일 덩치가 크다)
    for j in l:                              #중간에 하나씩 걸치다보면 랭크가 늘어나고
        if i[0] < j[0] and i[1] < j[1]:      #중복값이 나오더라도 문제가 안 된다
            rank += 1

    print(rank, end = " ")                   #가로출력을 위해 end 커맨드 추가