import sys
sys.stdin = open("input.txt", "r")

t=int(input())

for _ in range(t):
    n, m = map(int, input().split())
    nxn=[]
    res=0
    for b in range(n):
        nxn.append(list(map(int, input().split())))
        mxm=[]
        for i in nxn[b]:
            mxm.append(i)
            mxm.append(nxn[b][i+1])
            for j in nxn[b+1]:
                mxm.append(j)
                mxm.append(nxn[b][j+1])
                print(nxn)
                

    

        
        
#         result=max(res, sum(mxm))

    # print(f'{_}, result')

#이중리스트+완전탐색 문제라는 건 알겠는데 완전탐색 코드가 안짜진다..
#인덱스만 어떻게 잘 하면 될 거 같은데 내 맘대로 안되네..!