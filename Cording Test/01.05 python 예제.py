# 딕셔너리 활용 코드를 읽고, 출력 결과를 예측할 수 있다.
# 딕셔너리 순회 작동 방식을 이해하고, 순회 결과를 예측할 수 있다.
# 에러가 발생했을 때 에러의 원인을 설명할 수 있다.


1.

dict_variable = {}
dict_variable["이름"] = "정우영"
dict_variable["생년월일"] = "19000101"
dict_variable["회사"] = "하이퍼그로스"

print(dict_variable["이름"]) # 정우영
print(dict_variable["생년월일"]) # 19000101
print(dict_variable["회사"]) # 하이퍼그로스

print('==============================')

2.

dict_variable = {"a": "A", "B": "b"}
dict_variable["c"] = "C"
dict_variable["D"] = "d"
dict_variable["e"] = "E"


print(dict_variable["a"]) # A
print(dict_variable["D"]) # d 
print(dict_variable["b"]) # key error

print('==============================')

3.

dict_variable = {}
dict_variable["apple"] = 5000
dict_variable["banana"] = 3000
dict_variable["apple"] = 2000
dict_variable["banana"] = dict_variable["banana"] + 1000

print(dict_variable["apple"] + dict_variable["banana"]) # 6000

print('==============================')

4. 

dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

for key in dict_variable:
    print(key, dict_variable[key])

"""
이름 정우영
생년월일 19000101
회사 하이퍼그로스
"""

print('==============================')

5.

dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

for key, value in dict_variable.items():
    print(key, value)

"""
이름 정우영
생년월일 19000101
회사 하이퍼그로스
"""

print('==============================')

6. 

dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

print("나이" in dict_variable) # False

print('==============================')

7.

dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

if "거주지" not in dict_variable:
    dict_variable["거주지"] = "서울특별시"
    # dict_variable의 key 중 "거주지"가 있으면 수정하지 않고
    # 없는 경우 "거주지" key를 추가하여 value을 "서울특별시"로 한다
    
print(dict_variable) 

# {'이름': '정우영', '생년월일': '19000101', '회사': '하이퍼그로스', '거주지': '서울특별시'}

print('==============================')

8.

list_variable = []

try:
    list_variable.append(0)
    list_variable.append(1)
    list_variable.append(2)
    print(list_variable[3])
    
except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

"""
index error
python에서 리스트 순서대로 출력할 때 첫번째 자리를 0으로 지정하므로 list_variable[3]에 저장된 값이 없음
"""

print('==============================')

9.

try:
    number = 1
    if number == 1
        print(number)
    
    
except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

"""
SyntaxError
조건문 if인데 : 생략됨
빨간 제목 넘 신경쓰임
""" 

print('==============================')

10.

n = 10
total = 0

for number in range(0, n + 1):
    if number % 2 == 0:
        total += number * 2
    elif number % 2 == 1:
        total += number + 1 * 3

print(total) # 100 