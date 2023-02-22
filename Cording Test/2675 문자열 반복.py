t=int(input())

for i in range(1, t+1):
    r, s=input().split()
    p=[]
    for elem in s:        
        result=elem*int(r)
        p.append(result)
        P=''.join(p)
    print(P)

# n = int(input())

# for _ in range(n):
#     cnt, word = input().split()
#     for x in word:
#         print(x*int(cnt), end='')
#     print()  