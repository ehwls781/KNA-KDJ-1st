# 변수 선언 방법
# 변수이름 = 값
# 오른쪽 값을 왼쪽 이름에 "저장"하라는 코드
temp = 36 # 숫자는 따옴표 X
name = "센서 A" # 글자는 무조건 따옴표 O

print(temp) # 36
print("temp") # temp

# = 은 "같다"가 아니라 "저장"하는 것
# 비교는 "==" 을 사용

# =========================================

print("==== 변수 활용 ====")

x = 5
x = x + 5 # 변수를 재활용 할 때 기존 값을 활용할 수 있다
print(x)

# 변수에 할당할 때 오른쪽을 먼저 계사한 뒤 x의 값을 재할당
# y = y + 5 #오류 발생, 아직 y라는 정의가 없기 때문

# =========================================

print("==== 재할당 ====")

print("수정하기 전 temp :", temp)
temp = 15 # 위에서 사용한 36을 15로 수정
Temp = 150 # 대문자를 사용해 다른변수
print("temp:", temp, "Temp:", Temp)

# 재할당은 가장 마지막으로 지정된 값이 출력

# print(score) # NameError
score = 10
print(score) # 10
score = 20
score = 30
print(score) # 30

# =========================================

print("==== 값 복사 ====")

a = 10
b = a # b 변수에 10이 저장(저장할 당시에 a값을 저장
a = 100
print(b) # a값이 바뀌어도 b의 값은 10이 나온다

# =========================================

print("==== 여러 변수 한 번에 선언 및 할당 ====")

width, height = 10, 20 # width는 10, height는 20
print(width) # 10
print(height) # 20
# 형식 : 변수와 값의 갯수가 같아야 한다
# 변수1 : 값1 
# 형식과 값의 갯수가 다르면 valueError가 발생한다

# =========================================

print("==== 주석으로 변수 설명 ====")

temp = 25 # 온도(섭씨)
count = 3 # 센서 개수
# 이런식으로 값이 무엇을 의미하는지 주석으로 설명
# temp = 1000000 < 주석처리된 코드는 정상작동 X
print(temp) # 25
# 변수를 확인할 때 print로 값을 확인하고 수정하는 습관만들기

# =========================================

temp = 25
print(temp)
name = "센서a"
print(name)

temp = 30
print(temp)
temperature = 25
print(temperature)

my_number = 7
print(my_number)
mood = "피곤"
print(mood)

age = 27
lable = "기분"
print(lable)
print(age)

x = 10
print(x)
x = x + 5 # 15
print(x)
x = x * 2 # 30
print(x)

a = 100
b = a
a = 999
print(a) # 999
print(b) # 100
# b = a 라는 코드를 입력후 a = 999 라고 했기 떄문에 b의 값은 100

temp = 25
print(temp) #25
score = 90
print(score) #90

temp = 25 # 온도(섭씨)
count = 3 # 센서개수
# temp = 100 < 줄 앞에 주석이 있어 출력 X
print(temp) # 위 주석이 있어 temp = 100 이 성립이 되지 않아서 25가 나온다

x = 5
x = 10 # 위에 5라는 값은 없어짐
x = x + 1
print(x) # 11 < 

name = "김해" # 내가 사는 지역
temp = 24 # 내 나이
print("도시") # 그냥
print(name)
print(temp)

device_temp = 25 # 온도
sensor_count = 3 # 개수
print(device_temp)
print(sensor_count)

a, b, c = 1, 2, 3
me, you = 5, 10
print(me) # 5
print(you) # 10 
print(a)
print(b)
print(c)
# 변수와 값의 개수가 같아야 변수의 값이 정해진다

