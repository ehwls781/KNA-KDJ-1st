# 모듈 - 코드가 담긴.py 파일     
# 수학 관련 모듈을 불러옵니다
import math

# 해당 모듈이름.함수() 로 호출해야함
result = math.sqrt(16)
print(0)

# ===============================================

# 수학 관련 모듈에서 sqrt 기능만 불러옵니다
from math import sqrt

# 이젠 sqrt만 불러도 됩니다
result = sqrt(16)
print(result)


# --------------------------------------------

# math라는 모듈 이름 다 쓰기 귀찮아서 줄여본다
import math as mt

# 별칭으로 가져온 모듈 이름을 언급해보자
result = mt.sqrt(16)
print(result)

# datetime 모듈을 가져오자 !
import datetime

# detetime의 now()는 현재의 
# 지역 날짜와 시간을 반환
now = datetime.datetime.now()
print(now) # 2026-08-05 11:19:45.776780
print(type(now)) # <class 'datetime.datetime'>

# =====================================================

# 실습
import math
print(math.sqrt(16))  # 4.0

from math import sqrt as square_root
print(square_root(16))  # 4.0

import math as m
print(m.ceil(4.2))

# --------------------------------------------------------

# math 표준 라이브러리
import math

print(math.sqrt(9)) # 제곱근 값, 3.0
print(math.ceil(4.2)) # 올림값 5
print( 2 ** 3) # 2의 2승 = 2 * 2 * 2 = 8
# math에서 sqrt, ceil 두개만 사용하면
# 이렣게 사용해도 된다

from math import sqrt,ceil

# 위에서 가져온 math 함수들 사용 예제
print(sqrt(9)) # 3.0
print(ceil(4.2)) # 5

print( "= " * 20)

# 표준 라이브러리의 random 활용

import random

print(random.randint(1, 10)) # 무작위 정수
print(random.choice(["정상", "경고", "위험"]))

print(" ================================================ ")

# 표준 라이브러리의 datetime 묘듈
import datetime

# datetime 모듈 안의
# datetime 클래스에서 지원하는
# now() 함수 호출
now = datetime.datetime.now()
print(now)

print(" ================================== ")

# 모듈 도움말 보기 # 참고만 하고 구글링해서 보기
# dir(math)
# help(math.sqrt)

fake_r = random.randint(1, 112)
print(fake_r)  
print(math.sqrt(fake_r))

# 절대경로와 상대경로
# 정대경로의 예 : C:\uesrs\nedpark\바탕화면\sample\code.py

# 만약 C:\uesrs 폴더에 터미널을 연 상태에서
# code.py 코드를 실행하고 열고 싶다면
# python code.py

# 위 code.py 언급부분은 사실 상대경로를 의미한다
# 그래서 절대경로로 지정해줘도 똑같이 실행될 것이다

# 현재 경로에 있는 해당 파일이란걸
# 더 강조하는 상대경로 지정으로 써도 된다
# python ./code.py

# 만약 C:\uesrs\nedpark\바탕화면\sample 아닌
# C:\uesrs\nedpark\바탕화면\example 폴더 경로에서 코드를 실행하고 싶다면
# 절대경로 : python C:\uesrs\nedpark\바탕화면\sample\code.py
# 상대경로 : python ..\sampel\code.py

# 표준 라이브러리의 os 묘듈 활용
import os
current_working_directory = os.getcwd()
print(current_working_directory)

file_list = os.listdir()
for file_name in file_list:
  print(file_name)

print(" ======================================")
# 모듈 도움말 보기 : 참고만 하고 구글링한 웹사이트
# print(dir(math))
# help(math.sqrt)

# 파일이 존재하는지 확인
# 운영체제(윈도우/멕/리녹스)마다 경로를 나타내는 방법이 달라서
#  상황에 맞게 경로문자열을 만들어주는 os의 함수를 사용

path = os.path.join("data", "08_prees.csv")

# 실제로 경로문자열을 따라서 찾아가면
# 해당 파일이 있는지 확인: True/False
if os.path.exists(path):
  print(f"파일 있음: {path}")

# ===== 실습 3

practice_dir = 0
print(os.getcwd())
data_list = os.listdir(practice_dir)
for item in data_list:
    print(item)
    if item.endswith(".csv"):
        print("[csv]", item)

# === 실습 1
import math
print(math.sqrt(16))  # 4.0

from math import sqrt as square_root
print(square_root(16))  # 4.0

import math as m
print(m.ceil(4.2))

# === 실습 5.

file_count = len(os.listdir(practice_dir))
check_time = datetime.datetime.now()
print(f"파일 {file_count}개, 점검 시각 {check_time}")

# ==================================================================

