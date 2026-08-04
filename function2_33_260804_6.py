# 인삿말 출력 함수 간단 버전
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

# 인사할 대상이 많아진다고 위 함수들을 더 만드는건 좀 아니지않나?
# 해결책은 하나의 함수에서 저 다양성을 다 대응해주는 것
# 그것이 바로 함수의 매개변수 활용

def say_hi(name):
    print(f"반갑습니다, {name}")

say_hi("Ned")
say_hi("Tuna")
say_hi("Layla")

# 예제코드 : 특정 장비 이름을 알려주면 해당 장비의 체크를 시작 알림
def check(name):
    print(f"{name} 장비의 점검을 시작합니다")

check("압축기A")
check("펌프B")

# 매개변수가 2개 이상인 예제 - 덧셈
def calc_sum(number_a, number_b):
    # number_a = 1
    # number_b = 2
    total = number_a + number_b
    print(f"{number_a} + {number_b} = {total}")

calc_sum(1, 2)

# 매개변수가 2개 이상인 예제 - 장비 이름과 온도 정보 출력
def report(name, temp):
    # name = "압축기A"
    # temp = 75.3
    print(f"{name}의 온도는 {temp}도입니다.")

report("압축기A", 75.3)
report("펌프B", 85.2)

# 엉뚱하게 호출해봅시다
report(35.2, "보일러C")
# 첫번째 매개변수는 무조건 name이 되고, 
# 두번째 매개변수는 무조건 temp가 되니까
# 원하지 않는 결과가 나올 수도 있다

# 매개변수가 부족하거나 더 있으면? -> TypeError 발생
# report("압축기A", 75.3, "가동중") 
# report("펌프B")

# 키워드 인자
def report_keywords(name, temp):
    print(f"{name}의 온도는 {temp}도입니다.")

# 키워드 인자 없이 호출
report_keywords("펌프A", 37.4)
report_keywords(37.4, "펌프A") # 이 경우는 문제 발생

# 키워드 인자 사용해 호출 : 순서 바꿔 호출해 생기는 문제 근본 차단
report_keywords(name = "펌프A", temp = 37.4)
report_keywords(temp = 37.4, name = "펌프A")

# -----------------------
# 반환값

def add(a, b):
    total = a + b
    return total

print(add(1, 2))
print(add(11, 224))
print(add(13, 20))

# 여러번 같은 결과 호출해야한다면
# 차라리 변수에 담아서 쓰세요
result = add(1, 2)
print(result + 1)
print(result + 2)
print(result + 3)

# 평균 내는 함수 만들기
def calc_average(a, b):
    return ( a + b ) / 2

avg = calc_average(75.3, 88.0)
print(f"평균 온도: {avg}")

# 여러 값을 한 번에 반환하기
# 다음의 함수는 배열을 받아서 그 안의 최소값과 최대값을 동시에 return한다
def calc_min_max(values):
    minimum = min(values) # 배열 안의 최소값 찾아 minimum에 담기
    maximum = max(values) # 배열 안의 최대값 찾아 maximum에 담기
    return minimum, maximum

target_list = [1,2,3,4,5,6]
result = calc_min_max(target_list)
print(result) # 튜플인 것을 확인

# 반환값을 언패킹으로 받기
# 함수의 결과를 받는 순간에
# 결과 튜플의 내용을 풀어서
# 개별 변수에 담아 사용하기
result_min, result_max = calc_min_max(target_list)
print("최소값 " + str(result_min))
print("최대값 " + str(result_max))

# return 반환값이 없는 함수를 호출해놓고
# 결과를 어디에 담겠다고 하면, 
# 담기는 값은 None이 된다.

def say_greet():
    print("만나서 반가습니다")
    return

greet = say_greet()
print(greet) # None

# 실습 5 (선택문제)
# 내장 함수 min(), max(), sum(), len() 활용

# 지금까지 배운 내용을 활용

import random

groups = ["에스파", "하트2하트", "리센느", "태연", "엔믹스"]

# 랜덤 뽑기!
my_group = random.choice(groups)
print(my_group)


def get_random_group():
    groups = [
        {"이름": "에스파", "리더": "카리나"},
        {"이름": "엔믹스", "리더": "해원"},
        {"이름": "리센느", "리더": "원희"},
    ]

    my_group = random.choice(groups)

    return my_group.get("이름"), my_group.get("리더")


group_name, group_leader = get_random_group()
print(f"{group_name}의 리더는 {group_leader}입니다")
    


import random


def travel():
    country = [
        {"나라": "일본", "수도": "도쿄"},
        {"나라": "프랑스", "수도": "파리"},
        {"나라": "영국", "수도": "런던"},
        {"나라": "태국", "수도": "방콕"},
        {"나라": "미국", "수도": "워싱턴 D.C"},
    ]
    select = random.choice(country)
    return select.get("나라"), select.get("수도")


select_country, select_capital = travel()
print(f"환영합니다! {select_country} 나라의 수도는 {select_capital}입니다")

# 07_03 함수 설계와 활용

# 기본값 인자
# name과 value는 호출할 때 꼭 매개변수를 지정해줘야하지만 unit은 언급 안해주면 "도(C)"로 정해진다
def report(name, value, unit):
    print(f"{name}: {value}{unit}")

report("압축기A", 75.3, "도(C)")
report("압축기A", 75.3, "도(F)")

# 기본값 덮어쓰기
# 결과가 biilen 타입을 return하는 함수는
# 보통 is 로 시작한다

def is_danger(value, limit = 90):
    if value > limit:
        return True
        # 위험 맞음
    # 그 밖에는 위험 아님
    return False

print(f"위험한가요? {is_danger(95)}")
print(f"위험한가요? {is_danger(105)}")
print(f"위험한가요? {is_danger(20)}")


# 어쩌다가 다른 기준이 필요할 때만 새 기준을 전달

print(f"위험한가요? {is_danger(85, limit = 80)}")

# ===================== 실습 ===============================

# 기본값이 있는 메개변수를 만들고, 생략하면 기본값-넣으면 덮어쓰기를 확인

# def 괄호 안 메개변수에 =로 기본값 지정
# 인자를 생략하고 호출해 기본값이 쓰이는지 확인
# 인자를 넣어 호출해 기본값을 덮어쓰는지 확인
# 필수 매개변수는 앞, 기본값 매개변수는 뒤 순서 규칙 확인
# 앞선 예제 코드들이 잘 돌아가는지 확인하는 것으로 대체

# 실습 2. 지역변수와 범위
# scope !!!
# 코드의 어디부터 어디까지 이 변수 데이터가 살아있을까?

# 바깥동네에 변수를 하나 만들어봅시다
outter = 100

def change_outter():
    # 아래 코드는 함수 내부에서 처음 언급되면서
    # 새롭게 만들어진 내부의 outter이고
    # 함수가 종료되면 메모리에서 사라진다
    # 함수 바깥의 같은 이름의 존재에는 영향을 안준다
    outter = 50

change_outter()
print(outter) # 100

# 실습 3.
# 함수 안에서 만든 지역변수가 함수 밖에서는 보이지 않음 확인
# 앞의 예제코드로 확인 가능