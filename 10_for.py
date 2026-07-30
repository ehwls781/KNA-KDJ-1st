# 반복문은 동일한 작업을 특정 횟수만큼 반복해야할 때
# 코드를 길게 쓰지않고 반복시킬 수 있음

# for 변수 in range(횟수):
#   반복시킬 코드 (들여쓰기 한 칸 필수)
# 같은 코드를 복사 붙여넣기로 여러번 작서하는 대신
# "N번 실행하라"는 의미

for i in range(3):
  print("마치고싶다")
# i를 쓰지 않아도 됨 -> 목적이 "3"번 반복 하고싶을 때

# 0부터 10까지의 숫자 자체가 필요하거나 출력할 때
for i in range(11):
  print(i)  
# i는 증가값을 지정하지 않는 이상 반복할 때마다
# 자동으로 +1이 적용

# 짝수로 출력
for i in range(0, 11, 2):
  print(i) 
# 반복할 때 마다 2씩 자동으로 증가

# 홀수로 출력
for i in range(1, 11, 2):
  print(i)

# 역순으로 출력
for i in range(10, 0, -1):
  print(i)

# 10부터 1 까지 짝수만 역순으로 출력
for i in range(10, 0, -2):
  print(i)

# 실습
N =int(input("끝 숫자 : "))
for i in range(1, N + 1):
  print(i)
for i in range(2, N + 2, 2):
  print(i)
for i in range(N, 0, -1):
  print(i)

# 실습. 3의 배수 출력하기게임
# 사용자에게 범위를 입력받아 3의 배수 출력하기
# 예)
  # 사용자 입력값: 20
  # 출력값: 3, 6, 9, 12, 15, 18
# for문, if문, 나머지연산자

game = int(input("숫자입력: "))
for i in range(1, game + 1):
  if i % 3 == 0:
    print(i) # 3 6 9 12 15 18
  elif i % 5 == 0:
    print(i) # 5 10 20
# 3의 배수 식에서 15가 먼저 나와서 5의 배수를 구했을 땐 15가 나오지 않는다.

# ================================================================================='

# 누적변수

total = 0

for i in range(1,6): # 1 2 3 4 5
  total += i # total 에 i (12345) 더함 - 기존 total 값의 i(12345) 재할당
print("합계: ", total) # 15

# for문 안에 누적변수 선언 시

for i in range(1,6):
  total2 = 0 # 반복을 돌 떄마다 새로이 변수에 값이 0으로 할당
  total2 += i
print("합게: ", total2) # 가장 마지막 i 인 5가 출력되어 합계 : 5

# 번외편

if 3 == 3:
  hi = "안녕"
print(hi) # 안녕

# python에서는 if문 안의 변수도
# 어디서든 호출 가능한 변수로 선언

# 1~15 사이 4의 배수만 누적
total3 = 0
for i in range(1,16):
  if i % 4 == 0:
    total3 += i
print("1~15사이 4의 배수 누적: ", total3) # 24


# 초과하는 수의 갯수 구하기

cont = 0
for i in range(1, 13):
  if i > 5:
    cont += 1
print("5보다 큰 값의 개수: ", cont) # 7

# ====================================================================

# enumerate -낱낱이 세다

temps = [33, 23, 45, 32, 28]

for t in enumerate(temps):
  print(t)
# (0, 33)
# (1, 23)
# (2, 45)
# (3, 32)
# (4, 28)
# 범위를 지정하지 않아도 enumerate()에 전달한 리스트이 모든 요소 순회
# 문제는 형식이 (인덱스, 해당인덱스요소값으로 출력)
# enumerate() 사용할 때는 변수 2개 전달

for idx, t in enumerate(temps):
  print(f"idx: {idx}, t: {t}") 

# for idx,t in enumerate(temps):
# 위와 같이 전달하면 enumerate가 temps 리스트를 순회하면서
# 반환해준 (인덱스, 해당인덱스의값)을
#각자 idx에 인덱스값, t에 인덱스의 값을 할당
# 두개의 값을 바로 사용할 수 있게 해줌

for idx, t in enumerate(temps):
  print(f"현재 인덱스 : {idx}")
  print(f"{idx}인덱스의 값: {t}")
  print(f"{idx + 1}번째 반복 끝")


# 안녕의 인덱스 출력
# 이를 위해서 값을 비교하기위해 모든 리스트와 값이 필요
# 그리고 그 값의 인덱스를 알아야 출력가능

list = ["안녕", "hi", "hi", "안녕", "hi", "안녕"]

# 리스트의 모든 요소에 접근을 해야 하는 경우가 잦음
# 그래서 python이 반복문에서 이를 쉽게 할 수 있도록
# enumerate 내장 함수를 제공
# enumerate는 리스트의 모든 요소를 앞에서부터
# 순서대로 하나씩 찍어가면서 접근
# 접근해서 각자의 인덱스와 그 값을 뽑아준다 - 값은 2개
# 값을 두 개 받으니 우리도 변수를 2개 준비하면
# 각 변수에 쏙쏙 값이 할당
# 돌려주는 순서는 인덱스. 값 순으로 준다
# 그렇기 때문에 우리는 enumerate를 사용할 때
# for 뒤에 변수를 두개 전달

for index, value in enumerate(list):
  print(value)

list_len = int(len(list))
for i in range(len(list)):
  print(list[i])

# 위 두개는 똑같이 동작한다   


# ============================================
# 2단 출력하기
for su in range(1, 10):
  print(f"2 x {su} = {2 * su}")

# 1 ~ 5 단 출력하기
# 필요한 변수 : 2개 (몇 단 , 곱할 값)
# 몇 단 : 1 ~ 5
# 곱할 값 : 1 ~ 9
# for문 중첩 사용
# 1단은 유지한 상태에서 곱할 값은 커져야 함
# 1 x 1 = 1
# 1 x 2 = 2

# 단수를 유지하고 안에서 또 점점 커지는 변수가 있어야 하니
# 바깥 for문은 단수를 늘리고
# 안쪽 for문은 곱할 수를 늘리도록 구성

for i in range(1,6): # 1~5단 까지 반복
  for j in range(1, 10): # 1단에서 9단까지 곱하고 반복 종료
    print(f"{i} x {j} = {i * j}" )
  print(f"---{i}단 끝 ---")

# i단 끝

# =================================================================

for dan in range(1, 10, 1):   
    if dan % 2 == 0:          # 짝수 단만 출력
      for i in range(1, 10):
          print(f"{dan} x {i} = {dan * i}")

