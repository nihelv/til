# 1
a=input('')                 # 사용자 입력
b=list(a.replace(" ", ""))  # 사용자 입력에서 공백을 제외한 리스트 작성
c=1                         # 초기값이 0이 아닌 이유는
                            # list의 index를 구하는게 아니라서

for item in b:      # item이 b를 순회하는 동안
    if 'e' in item: # item 안에 'e'가 포함되어 있으면
        c = c       # c 변수를 c로 할당하고
        break       # 멈춰라.
    else:           # item 안에 'e'가 포함되어 있지 않으면
        c += 1      # c 변수를 c += 1로 할당하고 계속해라.
else:               # b를 전부 순회했는데 e가 없으면
    c=-1            # c 변수에 -1을 할당하고 끝내라

print(c)            # c 변수를 출력한다.