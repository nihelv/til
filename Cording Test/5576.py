import sys

sys.stdin = open("input.txt", "r")

w=[]
k=[]

for i in range(10):
    w.append(int(input()))

for _ in range(10, 20):
    k.append(int(input()))

w1=sorted(w)
k1=sorted(k)

w2=w1.pop()+w1.pop()+w1.pop()
k2=k1.pop()+k1.pop()+k1.pop()

print(w2, k2)
