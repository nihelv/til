# dice=list(map(int, input().split()))
dice=[2, 1, 5, 3, 4]

for n in dice:
    a= dice[dice.index(n)]
    b= dice[dice.index(n-1)]


    if b<=0:
        b=dice[0]
    
    elif n < a:
        b=b
    else:
        b, a=a, b
        print(dice)

# ???