# 산술연산자
# (+ - * / 목(//) 나머지(%) 거듭제곱(**))
print(3 + 5) # 8
print(10 - 4) # 6
print(4 * 5) # 20
print(20 / 4) # 5.0
print(7 // 3) # 2 (7/3 = 2와2분의1)이므로 //는 몫이기 때문에 2
print(7 % 3) # 1 (7/3 = 2와2분의1)이므로 %는 나머지기 때문에 1
print(2 ** 5) # 32 (2의 5제곱)

# ===============================================================

# 연산 우선순위와 우선순위 지정

# ** > *, /, //, % > +, - 순서로 우선순위가 정해진다.
print(2 + 8 * 3) # 8 * 3 연산후 2와 더한다
print((2 + 8) * 3) # 괄호 안의 연산을 먼저 계산한후 * 3 을 계산한다.

# ===============================================================

# 복합연산자

result = 3 * 5
print(result) # 15
# += : 기존 값에서 오른쪽 값을 더한 뒤 재할당 
# -= : 기존 값에서 오른쪽 값을 뺸 뒤 재할당 
# *= : 기존 값에서 오른쪽 값을 곱한 뒤 재할당 
# /= : 기존 값에서 오른쪽 값을 나눈 뒤 재할당 

result += 10 # 25
print(result)
result -= 5 # 20
print(result)
result *= 3 # 60
print(result)
result /= 2 # 30.0
print(result)

# ===============================================================

# 문자열 연산
print("안녕" + "하세요") # 안녕하세요

# 안녕하세요 사이에 공백을 추가하고 싶다면
# part 1
print("안녕", "하세요")
# part 2
print("안녕 " + "하세요")
# part 3
print("안녕" + " " + "하세요")
# 세가지 모두 같은 값인 ( 안녕 하세요 ) 가 출력된다

# 문자열 곱하기
print("안녕" * 5) # 안녕안녕안녕안녕안녕
#문자열에 연산자를 사용할 경우 이어져서 나온다.

# ===============    실  습    ===================

print(5 + 3) # 8
print(5 - 3) # 2
print(5 * 3) # 15
print(5 / 3) # 1.6
print(5 // 3) # 1
print(5 % 3) # 2
print(5 ** 3) # 125

mouse = 20
box = 30
Keyboard = 50
print(mouse + box + Keyboard) # 100
print(100 / 3) # 33.3
print(box ** 2) # 900
print(20 * 30 * 50) # 30000

# ===============================================================

# 비교연산자
# 미만, 초과, 이하, 이상, 같다, 다르다
# <, >, <=, >=, ==, !=

print(7 < 16) # True
# 비교 결과는 무조건 True or False (bool)
print(7 > 16) # False
print(7 <= 16) # True
print(7 >= 16) # False
print(7 == 16) # False
print(7 != 16) # True

# 비교연산자는 무자열 비교도 가능
print("hello" == "hello") # True
print("정상" != "정상") # False

# 1 대소문자 구분
print("hello" == "Hello") # False

# 2 공백이 있으면 다르다고 판단
print("정상" == "정상 ") # False

# 부정연산자 != (not)
print("hello" != "hello") # False (두 값이 동일한데 느낌표로 인해 값이 반대로 출력)
print("hello" != "hello" ) # True
print("hello" != "Hello") # True

# 변수에 문자열을 할당하고, 변수로 문자열 비교
hello = "hi"
# print(hello = "hi") # True
# 위 비교에서 hello는 따옴표로 깜사지지 않아서 "변수"로 취급
# 만약 hello를 "hello"와 같이 따옴표로 감싸면
# string으로 인식해서 변수 취급을 하지 않음 
# "hello"와 "hi"를 비교하는 것

# 변수로 비교연산자 사용
num1 = 123
num2 = 456

print(num1 >= num2) # False
# print(num1 >= "num2") # typeError

# 질문 1) hello 변수에 할당하는 값을 따옴표로 감싸지 않고 비교
# print("=== 질문 1) hello 변수에 할당하는 값을 따옴표로 감싸지 않고 비교 ===")
# hello = hi
# print(hello == hi)  # NameError(선언하지 않은 이름 호출했을 때)
# hi는 따옴표에 감싸져있지 않기 때문에 변수로 취급됨
# 그런데 우리는 hi 변수를 선언한 적이 없기 때문에 에러

# 질문 1) 해결방법
# print("=== 질문 1) 해결 방법 ===")
hi = "안녕"  # hello 변수에 hi 변수를 할당하기 전 hi 변수 선언
hello = hi  # print(hello) > 안녕
print("=== 변수 hello(안녕)와 변수 hi(안녕) 비교 ===")
# print(hello == hi)  # True

# =======================================================================

# and / or / not - 논리연산자
# and : 둘 다 True여야 True를 반환
print(5 == 5 and 7 == 7) # True
print(5 == 7 and 7 == 7) # False
# and는 천 번째 조건이 False라면 뒤에 조건은 확인을 안함
print(5 == 5 and 7 != 7) # False
# 위 코드는 가능 하다면 False가 먼저 오게 작성

# or: 하나라도 True가 있다면 True 반환
print(5 == 5 or 7 == 7) # True
print(5 == 7 or 7 == 7) # True
print(5 == 5 or 7 != 7) # or 는 첫 번째 조건이 True라면 뒤에 조건은 확인을 안함 < True 

# not: 값을 반대로 뒤집는다
print(not True) # False
print(not 5 == 5) # False 
# 5 == 5를 연산하여 True를 반환
# not True로 동작해서 True를 뒤집어 False를 반환
# False라는 값을 print가 터미널로 출력

# ==============================================================================

print(3 < 2) # False
print(3 <= 2) # False
print(20 >= 3) # True
print(20 >= 3) # True
print(20 == 5) # False
print(20 != 10) # True

temp = 85
print(temp > 80 and temp < 100) # True
print(not (temp > 90)) # True

ondo = 85
print(60 <= ondo <= 90) # True
enter = 5
print(3 <= enter <= 7) # True
print(3 == 3 and 7 == 7) # True

jaego = 100
jaego += 50 # 150
jaego -= 30 # 120
jaego += 5 # 125

total = 500
boolyrang = 23
print(boolyrang / total * 100) # 4.6 %
gadong = 21
modu = 24
print(gadong / modu * 100) # 87.5

sigan = 500
print(500 // 60) # 8h
print(500 % 60) # 20m  