1.

a=int(input('정수를 입력하세요 > '))

if (a >= 0):
    print(a)
else:
    print(a * -1)

print('==========================')


2.

# [1, 2, 3, 4] 라는 리스트를 받았다고 할 때

a=[1, 2, 3, 4]
c=0

for number in a:
    c += 1
print(c)
