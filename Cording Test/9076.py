# 점수 집계

t=int(input())

for i in range(t):
    num=list(map(int, input().split()))
    nums=sorted(num)
    if nums[-2] - nums[1] >= 4:
        print('KIN')
    else:
        nums.pop(-1)
        nums.pop(0)
        print(sum(nums))