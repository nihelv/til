#  1. 몫과 나머지 출력하기

T=int(input())

for t in range(1, T+1):
    a, b=list(map(int, input().split()))
    s = a // b
    y = a % b
    print(f'#{t} {s} {y}')


# 2. 평균값 구하기

T=int(input(''))

for t in range(1, T+1):
    n = list(map(int,input().split()))
    a = round(sum(n) / len(n))
    print(f'#{t} {a}')


# 3.

a, b = list(map(int,input().split()))

if 0 < a and b <10:
    z=a+b
    print(z)
    z=0
    z=a-b
    print(z)
    z=0
    z=a*b
    print(z)
    z=0
    z=a/b
    print(int(z))

    #일단 이게 실용성이 0이라는 건 알겠다. 억지로 값만 산출한거지..

