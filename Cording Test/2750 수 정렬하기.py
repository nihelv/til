num=int(input())
nums=[]

for n in range(1, num+1):
    nums.append(int(input()))

a=sorted(nums)

for s in range(1, num+1):
    print(a[s-1])