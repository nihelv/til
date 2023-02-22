import sys
sys.stdin=open('input.txt', 'r')

n=int(sys.stdin.readline())

nums=[]
result=1

for _ in range(n):
    a=int(sys.stdin.readline())
    nums.append(a)


m=nums[-1]

for i in reversed(nums):
    if i > m:
        result += 1
        m=i

print(result)

"""
1차시도 예외지정을 못해서 X
2차시도 상동
3차시도 상동
4차시도 시간초과(정답여부 알수없음)
5차시도 런타임에러(아래만 붙여넣어서 import sys를 안함)
6차시도 O
"""