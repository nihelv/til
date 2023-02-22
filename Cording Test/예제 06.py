T=int(input())

for test_case in range(1, T+1):
    a, b = list(map(int,input().split()))
    c=a+b
    print(f'Case #{test_case}: {a} + {b} = {c}')