T=int(input())

for i in range(1, T+1):
    # word=['I', 'am', 'happy', 'today']
    word=list(input().split())
    for elem in word:
        print(elem[::-1], end=' ')