T = int(input())
for test_case in range(1, T+1) :
    nums = list(map(int,input().split()))
    for n in nums:
        if n%2==1:
            s=sum(n)
            
print( f"#{test_case} {s}" )