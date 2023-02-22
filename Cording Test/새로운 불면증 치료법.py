t=int(input())
n=int(input())

for item in range(1, t+1):
    while True:
        for elem in range (1, n+1):
            l=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            m=list(sorted(set(list(map(int, list(str(elem * n)))))))
            if m==l:
                print(f'#{t} {str(m)}')
            else:    
                p=list(map(int, list(str(elem * n-1))))
                if n-1 == 0:
                    o=m
                    continue
                else:
                    o=m+p
                    continue

#이론은 그럴싸했는데...