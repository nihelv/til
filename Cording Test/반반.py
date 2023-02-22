import sys
sys.stdin=open('input.txt', 'r') # input.txt에서 불러온 값으로 input을 대체한다

t=int(input()) # t = 테스트 케이스 = input 받은 1자리 정수

for p in range(1, t+1): # 테스트 케이스를 순환. 동시에 print할 때 p를 변수로 표시할 것이기 때문에 1부터 시작해서 t+1로 range를 잡음
    s=input() # 알파벳 대문자로 이루어진 4글짜자리 문자열 s를 입력받음
    s1=list(set(s)) # s에서 중복을 제거한 값을 리스트로 만든다
    if len(s1) == 2: # 조건문 작성. s1에 남은 길이가 2이고
        if s.count(s1[0]) == s.count(s1[1]) == 2: # 동시에 s에서 s1의 첫번째, 두 번째 글자를 세었을 때 2가 나오는 걸 만족하면
            print(f'#{p}', 'Yes') # f스트링을 사용하여 #p Yes를 출력하고
        else:
            print(f'#{p}', 'No') # 각 요소의 카운트 값이 2가 아닐 경우 #p No를 출력하고
    else:
        print(f'#{p}', 'No') # 중복 제거 후의 리스트 길이가 3가 아닐 경우 #p No를 출력한다.

# if문 순서를 바꾸면 탐색 범위를 벗어났다고 나온다.
# 예시중에 len(s1)=1 인게 있어서 카운트 범위를 벗어나기 때문인듯