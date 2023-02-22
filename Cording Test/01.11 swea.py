# 2047. 신문 헤드라인

h=input()
# 헤드라인 문자열 입력
# 공백은 무조건 언더스코어로 입력하는 규칙인가?

result=""

for i in h:
    if i.islower() == True :
        w=i.upper()
    else:
            w=i
    result += w

print(result)


# 2025. N줄덧셈

a=int(input())
b=range(1, a+1)

print(sum(b))


# 1936. 1대1 가위바위보

p1, p2 = list(map(int,input().split()))
l1=[p1, p2]

for g in l1:
    if (p1 == (p2+1)%3) :
        print("A")
    elif (p1 != (p2+1)%3) :
        print("B")
    else:
        print('error')



# 2027. 대각선 출력하기

for i in range(5) :
    for j in range(5) :
        if i == j :
            print('#', end='')
        else :
            print('+', end='')
    print()



# 2058 자릿수 더하기

k = int(input())
sum = 0
for i in range(0, 4):
    if k <= 0:
        break
    j = k % 10
    k = int(k / 10)
    sum = sum + j
print(sum)


# 2019 더블더블

a = int(input())
for i in range(0, a+1):
    print(2**i,end=' ')






