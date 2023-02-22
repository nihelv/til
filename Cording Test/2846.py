n = int(input())
arr = list(map(int,input().split()))
start,end = arr[0],arr[0]
res = 0
for i in range(1,n):
    if end >= arr[i]:
        start = arr[i]      #여기 if문이 잘 이해가 안가는데 디버깅으로 역산 좀 돌려봐야 할 듯..
        end = arr[i]
    else:
        end = arr[i]
    res = max(res,end-start)
print(res)