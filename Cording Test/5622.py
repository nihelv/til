word=input()
# word='WA'
result=[]

for item in word:
    if item in ['A', 'B', 'C']:
        result.append(3)
    elif item in ['D', 'E', 'F']:
        result.append(4)
    elif item in ['G', 'H', 'I']:
        result.append(5)
    elif item in ['J', 'K', 'L']:
        result.append(6)
    elif item in ['M', 'N', 'O']:
        result.append(7)
    elif item in ['P', 'Q', 'R', 'S']:
        result.append(8)
    elif item in ['T', 'U', 'V']:
        result.append(9)
    elif item in ['W', 'X', 'Y', 'Z']:
        result.append(10)

print(sum(result))

# 쩜 무식하게 푼듯