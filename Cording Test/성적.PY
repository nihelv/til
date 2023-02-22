# import sys
# sys.stdin = open("input.txt", "r")

t=int(input())

for _ in range(t):
    n, m = map(int, input().split())
    nxn=[]
    res=0
    for b in range(n):
        nxn.append(list(map(int, input().split())))
        mxm=[]
        for i in range(n):
            mxm.append(nxn[i][i, i+1])
            for j in range(1, n):
                mxm.append(nxn[j][j, j+1])
                

    

        
        
#         result=max(res, sum(mxm))

    # print(f'{_}, result')

# #이중리스트+완전탐색 문제라는 건 알겠는데 완전탐색 코드가 안짜진다..