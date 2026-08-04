# 함수 오후 수업 

# 코드 중복과 함수화


# [상식]  - 사이드이팩트
# 특정 부분의 코드가 문제 없지만
# 다른 부분과 예상치 못한 영향을 주고받는다면?

print("압축기A 온도 확인 중")
print("결과를 기록합니다")
print("펌프1 온도 확인 중")
print("결과를 기록합니다")

# 위와 같은 식의 코드를 여기저기 복붙 하면
# 언젠가 사람의 실수로 사고가 생길 수 있다

def start_check():
  print("점검을 시작합니다")
  print("안전 장비를 확인하세요")
  print("기록을 준비하세요")

start_check() # 압축기A
start_check() # 펌프 1

# 함수의 호출 결과 예측하기

def say_hi():
  print("안녕하세요")

say_hi()
say_hi()

# 함수로 설비 점검 자동화
# 구분선을 출력하는 함수를 정의
# 점검 안내 여러 줄을 출력하는 함수를 정의
# 두 함수를 설비마다 순서대로 호출
# 실행해 각 설비마다 같은 안내가 반복되는지 확인
# 예상결과 : 구분선과 점검 안내 2줄이
# 설비마다 반복 출력

def print_line():
  print("=" * 20)


def print_check():
  print("점검 안내 출력")

# 장비 1에 대한 함수
print_line()
print_check()

# 장비 2에 대한 함수
print_line()
print_check()

# 인삿말 출력 함수 간단버전
def say_hello():
  print("안녕하세요")

say_hello()

# 인삿말 출력 함수 친근 버전
def say_hello_ned():
  print("안녕하세요, Ned")

def say_hello_tuna():
  print("안녕하세요, Tuna")

say_hello_ned()
say_hello_tuna()

# 인사할 대상이 많아진다고 위 함수들을 
# 더 만드는게 좋을까

# 해결책은 하나의 함수에서 다 대응해주는 것
# 그것이 바로 함수의 매개변수 활용

def say_hi(name):
  print(f"반가워요, {name}")

say_hi("Ned")
say_hi("Layly")

# 예제코드 : 특정 장비 이름을 알려주면
# 해당 장비의 체크를 시작 알림

def check(name):
  print(f"{name} 점검을 시작합니다")

check("압축기A")
check("펌프")

# 메개변수가 2개 이상인 예제 - 덧셈
def calc_sum(number_a = 1, number_b = 2):
   total = number_a + number_b 
   print(f"{number_a} + {number_b} = {total}")

calc_sum(1, 2)

