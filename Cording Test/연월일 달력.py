day= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T=int(input())
for i in range(1, T+1):
    a=input()
    m=int(a[4:6])
    d=int(a[6:8])
    result= '-1'
    if 1<=m and m<=12 and 1<=d and d<=day[m-1]:
        result=a[0:4]+"/"+a[4:6]+"/"+a[6:8]
    print(f'#{i} {result}')