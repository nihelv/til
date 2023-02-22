"""
조건문 내부에서 실행되는 코드 블럭이 무엇인지 알고 있다.
반복문 내부에서 변수가 어떻게 변화하는지 예측할 수 있다.
파이썬 내장 함수의 결과를 예측할 수 있다.
"""


list_variable = [0, 1, 2, 3, 4, 5, 6]
list_variable.pop()
list_variable.append(7)
list_variable.append(8)

for element in list_variable[2:]:
    print(element, end=" ")
    
"""
2 3 4 5 7 8
"""


for element in range(-2, 10, 2):
    print(element, end=" ")
    
"""
-2 0 2 4 6 8
"""


a, b, c, d = 0, 0, 0, 0
n = 10

for number in range(n):
    if number % 2 == 0:
        a = a + 1
        
    if number % 3 == 0:
        b = b + 1
        
    if number % 4 == 0:
        c = c + 1
        
    if number % 5 == 0:
        d = d + 1

print(a, b, c, d) 

"""
5 4 3 2 1

이거 좀 헷갈림 4부터는 두번 더하는 거 맞나?
"""



i = 0
while i <= 10:
    print(i)
    i = i + 1

"""
0
1
2
3
4
5
6
7
8
9
10
"""


i = 0
while i <= 10:
    i = i + 1
    print(i)

"""
1
2
3
4
5
6
7
8
9
10
11
"""


i = 0
while i <= 10:
    i = i + 2
    print(i)

"""
2
4
6
8
10
12
"""


i = 0
while True:
    print(i) 
    i = i + 1
    if i > 10:
        break

"""
0
1
2
3
4
5
6
7
8
9
10
"""


i = 0
while True:
    print(i) 
    if i > 10:
        break
    i = i + 1
    
"""
0
1
2
3
4
5
6
7
8
9
10
11
"""


list_variable = [0, 1, 2, 3, 4, 5, 6]
print(len(list_variable)) # 7


list_variable = [0, 1, 2, 3, 4, 5, 6]
print(sum(list_variable)) # 21


list_variable = [3, 1, 4, -3, 9, 7]
print(min(list_variable) - max(list_variable)) # -12