"""
문제에서 주어지는 입력을 받기 적합한 입력 코드를 작성하세요.

입력과 동일하게 출력하는 코드를 작성하세요.
"""

# 1.

n=int(input(''))
print(n)


# 2.

a, b = input('').split()
print(a + ' ' + b) 

"""
문자열은 안된다고 한 적은 없으니까 출력만 똑같이 보이게 꼼수를...
앞으론 정수취급 하겠습니다ㅋㅋㅋㅋ
"""


# 3.

n=list(map(int, input('').split()))
print(*n)


# 4.

a=input('')
b=input('').split()
c=[]

for i in b:
    c.append(a + i)

print(*c)


# 5.

n=list(map(int,(input('').split())))
print(*n)


# 6.

h=list(map(int,(input('').split())))
l=[]

for item in h:
    l.append(item)
    l.append(item * -1)

print(*l)


# 7.

n1=list(input('').split())
print(*n1)


# 8 9

n=list(map(int,(input('').split())))
print(*n)

