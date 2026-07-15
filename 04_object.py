# int, float, str, bool, type 사용법

# int - 정수형

count = 3
age = 20
tall = 173

temp = -30
zero = 0

# 소수점 없이 딱 떨어지는 수를 정수형이라고 한다
# 0 or 음수도 정수에 포함 

# =========================================================

# flolt - 실수형
# 소수점이 붙어있는 숫자를 실수형이라고 한다
# 5.0과 같이 딱 떨어져도 소수점이 있으면 실수형이라고 한다

tired = 99.9
height = 17.2

# =========================================================

# string - 문자열형
# 따옴표에 감싸져 있는 모든 값

hello = "안녕하세요"
emoji = "★"
empty = ""
fake = "1234"
boat = "2.2"
illit = "it's me" # 작은 따옴표가 글자에 사용되고 있다면 큰 따옴표로 문자를 덮어주기 

# 따옴표에 감싸져있기라도 하면 string이 된다.
# 숫자도 따옴표에 감싸져 있다면 글자로 인식을 해 string이 된다.
# ''와 ""둘다 사용 가능하지만 문자를 덮을 때 다른 것을 사용하면 안된다
# '바보", "엥' 식으로 따옴표 크기가 안 맞으면 안됨

# =========================================================

# bool - 불리언형
# True 와 False만 사용가능
# 첫 글자는 대문자로, 따옴표 없이 사용

ok = True # 진실
no = False # 거짓

# 비교할 경우 사용하는 TIP
print(100 < 5) # False      
print(100 == 100) # True
print(100 > 50) # True

# =========================================================

# type() - 자료형 확인
# type(값) < 확인하려는 것 -> 입력한 것의 자료형을 알려준다

type(5) # 터미널에서 확인 불가 -> print하지 않았기 때문

print(type(5)) # 이런식으로 print 사용해야 확인가능 -> <class 'int'> 라고 결과출력
print(type("센서A")) # <class 'str'> 라고 결과출력
print(type(True)) # <class 'bool'> 라고 결과출력

print(type(3 > 2)) # <class 'bool'> 라고 결과출력
# 1. print함수의 내부를 확인
# 2. print함수에 또 함수가 있는 것을 확인하고 type 함수의 내부를 확인
# 3. type 함수 내부에 연산자가 있는 것을 확인하고 연산 진행
# 4. 3>2의 연산 결과는 True이기 때문에 type(True)로 바뀜
# 5. type(True)의 결과인 <class 'bool'>이 print로 인해 터미널에 출력

print(3, type(3)) # 3, <class 'int'> 라고 출력

num = 123
fake_num = "123"
str = "문자열"
ok = True

# 변수 확인 및 자료형 확인
print(num, type(num)) # 활용할 때는 알고 싶은 변수와 변수가 어떤 형인지 확인 할 수 있다
print(num, ":", type(num)) # 123 : <class 'int'>라고 터미널에서 알기 편한 코드

# 찾기 쉽게 하는 방법
print("num :", type(num)) # num : <class 'int'라고 출력됨

# =========================================================

# 자료형마다 동작 다른 것 확인

print(3 + 5) # 8 (int) > 숫자끼리 더하기는 계산
print("3" + "5") # 35 (str) > str끼리 계산은 이어 붙임
print("안녕하" + "세요") # 안녕하세요 (str)


# print로 자주하는 실수
print(0.1 + 0.8) # 0.9 (가끔 연산오류로 오차발생 할 경우도 있음)

# round 사용법
print(round(0.1 + 0.8, 2)) # round를 사용해주고 자릿수를 같이 넣어주면 반올림해서 출력

# str, int, float : 덧셈 불가
# print('123' + 456) # TypeError 발생

# 나눗셈은 결과가 딱 떨어져도 무조건 float
print(10 / 2) # 5.0
print(type(10 / 2)) # <class 'float'>

# =========================================================

print(3 + 3) # 6 (int)
print(100 / 2) # 50.0 (float)
print("hy") # hy (str)
print(100 > 58) # True (bool)


print(type(6)) # <class 'int'>
print(type(100 / 2)) # <class 'float'>
print(type("hy")) # <class 'str'>
print(type(100 > 58)) # <class 'bool'>

# print(100) # int
# print(100.0) # float
# print("100") # str
print(type(100)) # <class 'int'>
print(type(100.0)) # <class 'float'>
print(type("100")) # <class 'str'>

print(100 + 100) # 200
print("100" + "100") # 100100
# print("100" + 100) # TypeError

# print(3 > 2)
print(3 > 2) # True
print(5 == 5) # True
print(type(3 > 2)) # <class 'bool'>
print(type(5 == 2)) # <class 'bool'>

boy = 24
print(type(boy)) # <class 'int'>
boy = 24.7
print(type(boy)) # <class 'float'>
boy = "24"
print(type(boy)) # <class 'str'>

device_temp = 20 # int
check_count = 30.0 # float
device_name = "KDJ" # str
is_normal = True # bool

# =========================================================

# 연산을 활용할 때 목(//)과 (%)나머지를 구하는 방법

# print(7 // 2) < 3(몫)
# print(7 % 2) < 1(나머지)
# 보는 것 처럼 나누고 싶은 값을 목(//) 또는 나머지(%)를 활용

# 거듭제곱(**)을 구하는 방법

# print(2 ** 2) 8

# 연산자 우선순위

# print(2 + 3 * 4) # 14
# print((2 + 3) * 4) # 20
# 괄호를 사용해 +를 먼저 계산할 수 있게 사용

# 계산을 변수에 저장하는 Tip

# re = 3 + 5
# print(re)
# avg = ((80 + 90) / 2)

# 복합 할당 연산자(+-) 사용

# score = 100
# score += 10 < 110
# score -= 10 < 100
# +로 하고 -도 해서 복합 연산자라고 얘기

# score *= 5 < 500
# score /= 2 < 250
# 나눗셈과 곱셈도 사용 가능


# =========================================================

# 문자열 연결법

# print("안녕" + "하세요")
# print("안녕 " + "하세요")
# print("안녕" + " " + "하세요")
# print("안녕", "하세요")
# 위 4가지 모두 (안녕 하세요)로 출력된다

# print("하" * 3) # 하하하
# 문자를 곱할수도 있다

# ================  비교  연산자  =====================

# 결과는 항상 True , False 로 나온다. (bool)
# print(5 == 5) # True
# print(5 != 3) # True 
# != : False 로 사용할 수 있다

# 크기비교를 할 때는 >=, <= 로 이상,이하도 사용할 수 있다.
# 꼭 숫자열이 아니라 문자열도 비교를 할 수 있다. < 공백과 대소문자가 같아야 True가 나옴

# =========================================================




