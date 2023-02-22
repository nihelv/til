s1=int(input())
s2=int(input())
s3=int(input())
s4=int(input())
s5=int(input())

s_l1=[s1, s2, s3, s4, s5]
# s_l1=[10, 65, 100, 30, 95]
s_l2=[]

for s in s_l1:
    if s <= 40:
        s_l2.append(40)
    else:
        s_l2.append(s)

A=int(sum(s_l2)/5)
print(A)