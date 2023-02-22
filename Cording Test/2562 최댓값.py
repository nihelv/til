num=[]

for n in range(9):
    num.append(int(input()))

x=num[0]

for i in num:
    if i > x:
        x = i

print(x)
print(num.index(x)+1)


