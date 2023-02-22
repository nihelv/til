
t=int(input())
a=int(input())
result=0

for _ in range(t):
    b = list(input())
    for i in range(a):
        if b:
            if b[0] == '(':
                b.remove('(')
                b.remove(')')
            elif b[0] == '[':
                b.remove('[')
                b.remove(']')
            elif b[0] == '<':
                b.remove('<')
                b.remove('>')
            elif b[0] == '{':
                b.remove('{')
                b.remove('}')

    if len(b) == 0:
        result += 1
        print(f'#{_}', result)
    else:
        print(f'#{_}', result)

# 조금만 더 고치면 될 거 같아서 조금만 조금만 하다가 두시간 넘게 붙들고 있었음.
# 코드를 세 번 넘게 엎었던 거 같다
# 어케저케 얼레벌레 답은 나오는데 SWAE에서 런타임오류라고 한다..