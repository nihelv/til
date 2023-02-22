i = int(input())
nums = list(map(int, input().split()))
r_max = nums[0]
r_min = nums[0]

for n in nums:
    if n > r_max:
        r_max = n
    elif n < r_min:
        r_min=n
    else:
        r_min=r_min
        
        
print(r_min, r_max)