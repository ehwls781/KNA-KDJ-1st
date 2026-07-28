# """ """ - 여러 줄 문자열

notice = """설비 점검 안내
1. 전원 확인
2. 센서 점검 """

print(notice)
# 설비 점검 안내
# 1. 전원 확인
# 2. 센서 점검
# 위와 같이 직접 작성한 줄바꿈이 반영되어 여러줄로 출력함

notice = """설비 점검 안내
1. 전원 확인
2. 센서 점검 
"""

# 개발자가 보기 편한 방식으로 작성하면 생각과 다른 결과물이 나온다.
#""" """ - (삼중 따옴표를 사용할 시 그 내부의 모든 줄바꿈이 다 반영되서 출력)

# 탭
notice = """설비 점검 안내
  1. 전원 확인
2. 센서 점검 
"""
 # Tab을 사용했을 때 Tab도 그대로 유지가 된다

# ====================================
# 이스케이프 문자

# notice 이스케이프 사용해서 개선
notice = "설비 점검 안내\n1. 전원 확인\n2. 센서 점검"
print(notice)

tap = "이름\t상태" # 이름      상태
print(tap)
print("이름 상태")

backslast = "이름\\상태"
print(backslast) # 이름\상태 > 첫 번째 \는 이스케이프 문자라는 것을 알리는 용도

quotes = 'It\'s me' # 감싸는 따옴표와 str 내부 따옴표의 종류가 같을 때는 \ 사용
print(quotes)

# 빈 문자열과 공백 문자열의 차이
# 따옴표로 감싸졌지만 아무것도 적지 않으면 빈 문자열
# 따옴표로 감싸졌지만 공백(space bar)이 들어가있으면 공백 문자열
# 공백(space bar)의 수 만큼 글자가 있고,길이가 세어짐
# 빈 문자열과 공백 문자열은 컴퓨터에게 다른 값으로 인식된다
print("" == " ") # False

sulbi = "설비 점검 안내\n1. 설비:\n2. 가동:\3. 점검날짜"
baba = "PUMP_A"
coco = "정상"
gaga = 1200
dayday = "2026 - 07 - 16"
card = "상태: " + baba +"\n상태: " + coco +"\n가동: " + str(gaga) +"\n점검날짜: " + dayday
print(card)
 
 # ===================================================================================

# 인덱싱 ?!?!?!?!?!??!!!?!

# 위치 번호로 글자를 하나 꺼내기
# 문자열 [인덱스번호]
# 문자열의 첫 글자 인덱스는 0

word = "PYTHON"
print(word[0],word[3],word[5]) # P H N

abc = "abcdefghijklnmopqrstuvwxyz"
print(abc[3], abc[14], abc[9], abc[8], abc[12]) # d o j i n

# 음수 인덱스는 뒤에서부터 역순으로 순서 숫자가 붙는다
# 주의사항 ) 음수 인덱스는 가장 마지막 글자가 -1부터 시작
# IndexError가 뜨지않게 주의 ~
# 주의사항 ) 양수 인덱스는 0부터 시작하니 주의하기 !!!!!!!!

# ===================================================================================

# 슬라이싱 ★중요★
# 구간으로 잘라내기
# 문자열[시작:끝]

# ex) wdrd = "PYTHON"
# print(wodr[1:4]) < YTH <- 마지막 숫자인 4번째 는 나오지 않는다.
# 가장 마지막 번호에서 +1 을 해야 마지막 번호까지 가져올 수 있다.

print(word[3:6]) # HON

# print(word[6]) # 인덱싱은 정확하게 마지막 인덱스 까지만 쓸 수 있고, 넘치면 Error
# 슬라이싱은 end가 포함되지 않고 출력하기 때문에 없는 인덱스인 6도 사용

# 슬라이싱 - start 생략 
# 처음부터 특정 인덱스까지 구간을 뽑아내고 싶을 때 사용
print(word[:4]) # print[word[0:4]]와 같다

# 슬라이싱 - end 생략
# 특정 인덱스부터 끝까지 뽑아내고 싶을 때 사용
print(word[2:]) # 2번 인덱스부터 끝까지 출력
# print(word[2:6])와 같다

# 슬라이싱 - 전체 생략
print(word[:]) # word가 전체 출력된다

# 슬라이싱 - 음수 인덱스 사용
print(word[-3:]) # HON
# 음수 인덱스 작성 시 그 인덱스 부터 정방향으로 출력함
print(word[:-1]) # PYTHO
# 처음부터 -1(5)를 제외한 구간을 뽑아냄 <- 역순 아님 !!
# 음수 인덱스 사용 시 컴퓨터가 알아서 정수 인덱스 찾아 치환해서 동작

# step으로 건너뛰기
# 문자열[시작:끝:간격(step)]
print(word[0:6:2]) # PTO (ex) PYTHON 에서 2간격으로 PTO가 출력
# 첫 번째 글자가 0인데 0부터 기준을 잡아서 출력
# step이 2이기 때문에 T 뛰고 T 출력 후 H 뛰고 O 출력 후
# N 뛰고 끝 
# 두 글자를 뛰는게 아니라 2 번 뛰는 것
# 주의사항 -> 간격을 1로 하면 모든 것이 출력

# start와 end를 생략하고 step만 입력
print(word[::2]) # PTO
# word 변수의 모든 글자를 두 칸씩 뛰면서 출력

# 순서 뒤집기
print(word[::-1]) # NOHTYP 역순으로 출력이 된다
# step = 인덱스가 아니라, 음수 입력 시 문자열의 순서를 뒤집음

# 슬라이싱은 범위를 벗어나도 오류가 발생하지 않는다
print("범위를 벗어난 슬라이싱", word[0:100]) # PYTHON

# ==============================================================

mic = "stars"
print(mic[0:2]) # st
print(mic[2:4]) # ar

mog = "Posco_Data"
print(mog[:5]) # Posco

mog = "Posco_Data"
print(mog[6:]) # Data


note = "Choco"
print(note[-1:0])

mouse = "PYTHON" # PTO
print(mouse[::2])

mouse = "PYTHON"
print(mouse[::-1]) # NOHTYP

# ==============================================================
# len() - 문자열의 길이 반환
# len(문자열) 

print("=== len() 활용 ===")

print(len("Hello World")) # 11 -> 10글자이지만 공백을 포함해서 11이 나온다
print(len("")) # 0 (빈 문자열은 0 출력)

var = "한 시간만 더 하면 된다. 조금만 버티자 !"
print(len(var)) # 24 -> 변수에 담긴 문자열의 길이도 출력 가능 !

print(len("이것도") - len("가능할까")) 
# len()은 int를 반환하기 때문에 연상 가능

print("길이:", len(abc), "/ 마지막 인덱스 번호:", len(abc) - 1) # 길이: 26, 마지막 인덱스 번호: 25

# 음수 인덱스를 쓰지 않고 마지막 인덱스 문자를 출력하고 싶을 때
print(abc[len(abc) - 1]) # z

num = "01011223344"
print(len(num)) # 11

# ================================================================
# in - 특정 단어가 들어 있는지 True - Flase 로 확인
# 찾을문자열 in 문자열
print("고장" in "설비 고장 발생") # True
print("정상" in "설비 고장 발생") # False
print("설비에서 고장" in "설비 고장 발생") # False
print("설비에서 고장" in "설비에서 고장이 났습니다.") # True

# not in - 특정 단어가 안 들어 있는지 확인 
# 들어 있으면 False, 없으면 True

print("고장" not in "설비 고장 발생") # False
print("정상" not in "설비 고장 발생") # True
print("설비에서 고장" not in "설비 고장 발생") # True
print("설비에서 고장" not in "설비에서 고장이 났습니다.") # False

print(" " in "설비 고장 발생") # True
# 따옴표로 감싼 공백(space bar)는 "한 글자"로 취급 되기 떄문

# ===============================================================

print("=== count ===")

# .count() - 문자열에 특정 글자의 수(int)를 반환
# 문자열.count("찾을 글자") -< count 사용 방법
print("banana".count("a")) # 3
print("01012341234".count("12")) # 2
print("layla@spreatics.com".count("@")) # 1 <- 이메일 확인 방법 !

print("banana".count("na")) # 2

# =============================================================

print("==== find() ====")

# .find() - 특정 글자가 처음 나오는 위치를 반환
# 있으면 숫자가 나오고 없으면 -1 이 나온다.

email = "hong@cp.com"
at = email.find("@") # @ 위치의 인덱스인 4가 할당
user_id = email[:at]
print(user_id)

mouse = "machinda@pipa.com"
ab = mouse.find("@")
print(mouse.find("ab")) 
print(mouse.find("pass")) 

# SQE-00Q8 이라는 설비의 SQE만 뽑아내기
SQE = "SQE-00Q8"
# SQE_index = SQE.find("SQE")
# print(SQE_index) # 0

SQE_index = SQE.find("-")
print(SQE_index) # 3
SQE_fin = SQE[:SQE_index] # SQE[0:3] > SQE
print(SQE_fin) # SQE

# ==================================================================

# index() 
# 특정 문자열의 위치(인덱스 번호)를 반환
# 앞에서 부터 가장 처음 나오는 인덱스 번호만 반환
# 찾는 문자열이 없으면 Error 발생

email = "ehwls781@naver.com"
at = email.index("@") # 5
print(email[0:at]) # ehwls781 - 시작 번호가 0이라면 start 생략 
print(email[at+1:]) # 끝까지 출력하고 싶고, 뒤에 몇 글자가 있는지 모르니 생략

# find에서 했던 SQE 뽑아내기 실습

cs = "E200-008"
csv = cs.index("-")
csb = cs[:csv]
print(csb)

# ===================================================================

# count()
# 문자열에서 특정 문자열의 갯수 세기

str1 = "a, b, c, d, e,a, a"
print(str1.count("a")) # 3
print(str1.count(",")) # 6
print(str1.count(", ")) # 5 -> count로 찾는 문자열과 동일해야 갯수를 셈

# ====================================================================

# startswith()
# 특정 문자열로 시작하는지 검사 후 True/False (bool)

print("E200-008".startswith("E200"))

# 변수 활용
e200 = "E200"
print("E200-008".startswith(e200)) # 변수명은 따옴표로 감싸면 안된다.!!!!!!!!!!

# ======================================================================

# endswith()
# 특정 문자열로 끝나는지 확인
# True / False로 반환

str2 = "월요일입니다! 여러분은 할 수 있어요!"

print(str2.endswith("!")) # True
print(str2.endswith("요!")) # True
print(str2.endswith("음")) # False
print(str2.endswith(" 월요일입니다! 여러분은 할 수 있어요!")) # False
print(str2.endswith("월요일입니다! 여러분은 할 수 있어요!")) # True
print(str2.endswith("월요일입니다!   여러분은 할 수 있어요!")) # False 

# ===============================================================

hsg = "sensor_log.csv"
print(hsg.startswith("sensor"))
print(hsg.endswith(".csv"))

# ===============================================================

print(type("잊어먹으면 안돼")) # class 'str'
print(len("이렇게 썼죠")) # 6
# endswith와 len의 차이점
# endswith는 .으로 연결
  # .으로 연결하는 이런 도구들은 "메서드"
  # 문자열이나 int, float처럼 특정 자료형(객체) 내부에 포함된 기능
# len은 . 사용 안함
  # () -> GKATN
  # LEN과 같이 개발자가 직접 선언하지 않은 기본 제공 함수 : 내장함수

"str".startswith("s")
# 123.startswith(1) 
# .으로 사용하는 메서드들은 특정 자료형(객체)마다 다르다
# int 자료형의 객체에는 startswith라는 메서드가 없다

# print(len(123)) -> Error

# ==============================================================

# 메서드 - 특정 자료형(값=객체)에 소속된 함수
# 문자열.메서드이름()
# 추가 정보가 필요하면 괄호 안에 인자 (count('a'))
# 인자 없으면 괄호만 비워 둠
# word = "python"
# print(word.upper()) # python
# print(word.count("p")) # 1
# print(word.startswinth("p")) # True

# ===============================================================

num = 1
num = num + 1 # 2
num += 1 # 3
# += 복합할당연사자로 원래 내 자신의 값에 다음 오는 연산자와 값을 적용해서 재할당

# ====================================================================

# .upper() - 영문 글자를  모두 대문자로

str3 = "abcdefg"
print(str3) # abcdefg

str.upper # ABCDEFG -> 반환은 대문자인데, 값에 재할당은 x
print(str3) # abcdefg -> 기존 str3의 값인 소문자를 그대로 출력

# 앞으로 계속 대문자로 변환한 값을 사용하고 싶다면
# 변수에 재할당을 해야함
# 변수 재할당에서 변수 스스로를 부르는 것이 가능
# 재할당에서 변수 스스로 값을 부르려면 "재할당" 이어야 한다

str3 = str3.upper()

# 최초 변수 할당 시에는 저장된 값이 없어서 변수 스스로 할당 불가능

aug = "babo"
bobo = aug.upper()
print(bobo)

# lower() - 영문 글자를 모두 소문자로

a = "Warning"
b = a.lower()
print(b)

# capitalize - 문장 철 글자만("python is" > "Pythom is")
# title - 단어 마다 첫 글자("hong gil" > "Hong Gil")

user_name = "kim chul su"
print(user_name.capitalize()) # Kim chul su
print(user_name.title()) # Kim Chul Su

# '를 사용한 경우
print("i'm full".title) # I'M Full

# isupper - islower() 
print("ABC".isupper())
print("abc".islower())
print("Abc".islower())

fama = "Sensor_LOG.CSV"
mama = fama.lower()
print(mama.startswith("sensor"))
print(mama.endswith(".csv"))

# ===========================================

# .strip () - 문자열의 앞뒤 공배을 떼어 줌
# .lstrip() - 왼쪽 공백만 제거
# .rstrip() - 오른쪽 공백만 제거

raw = "   정상    "
print(raw.strip()) # 정상
print(raw.lstrip()) # "정상    "
print(raw.rstrip()) # "    정상"

print("    정   상    ".strip) #   정    상 

print(raw)  #  "   정    상    "
  # strip은 재할당이나 새 변수에 할당하지 않는 이상 휘발

# strip으로 문자 제거
str4 = "===정상==="
print(str4.strip("=")) # 정상
# 인자로 전달한 양 끝의 =이 모두 지워짐

str5 = "=정상====="
print(str5.strip("=")) # 정상
# 갯수 상관 없이 인자로 전달한 문자를 무조건 삭제
print(str5.strip("= ")) # 정상
# strip 자체가 공백을 지우는 것이기 떄문에 공백 상관없이 양 끝의 해당 문자열 삭제

str6 = "==정==상===="
print(str6.strip("=")) # 정==상
# 글자 중간에 있는 문자열은 건드리지 않는다

# strip으로 못 지우는 중간 공백을 
# replace로 해결!!!!!!!!!!!!

# ===================================================

# 체이닝 x
raw = "    NORMAL    "
step1 = raw.strip() # NORMAL
step2 = step1.lower() # normal

# 체이닝 x, 기존 변수에 재할당
raw = raw.strip() # NORMAL
raw = raw.lower() # normal

# 체이닝 o
chain = raw.strip().lower() # normal

# 기존 변수에 재할당도 가능
raw = raw.strip().lower() # normal

# 변수에 할당하지 않고 사용 가능
print(raw.strip().lower()) # normal

phone = "   Warning   "
iphone = phone.lower()
print("[" + iphone + "]")
iphone = phone.strip().lower()
print("[" + iphone + "]")

# strip() 메서드에 인자로 들어가는 문자열은 완전히 동일하지 않아도 전부 삭제

str7 = "aaab 이렇게? cd"
print(str7.strip("abcd")) # " 이렇게?"" 
print(str7.strip("abcd ")) # "이렇게?"
print(str7.strip("bc")) # "aabb 이렇게? cd"
print(str7.strip("ab")) # " 이렇게? cd"

# GPT한테 질문을 하면서 이해를 하는법
str7 = "aaab 이렇게? cd"
print(str7.strip("abcd")) # " 이렇게? "

# 지금 출력 결과는 " 이렇게? " 나오고 있어
# 내가 생각했을 떄 == 처럼 정확하게 "abcd" 순서가 아니면
# strip이 안될 줄 알았는데 실행 결과를 보니 순서랑 상관없이
# 인자로 전달한 문자열에 해당하는 글자가 확인하는 문자열 양 끝에
# 하나라도 있으면 동작하는 것 같아.
# 내가 이해한게 맞아 ?
# 그러면 왜 이렇게 동작하는거야 ?

# =================================================================

# replace() - 특정 글자, 단어를 다른 것으로 바꾸기
# replace(" ","") -> 중간 공백 제거
# "010-1234-1234".replace("-","")
# text = "정 상 가 동"
# text = text.replace(" ","") # 공백제거
# print(text) # 정상가동
# 체이닝으로 연계도 가능 !
# "fault""FAULT"를 모두 "고장"으로 통일
# "3,000"의 쉼표를 제거해 int로 변환 가능

print(" 정 상 가 동".replace(" ","")) # 정상가동 -> 모든 공백 제거 !
print("  정     상 가 동".replace("  ","")) # 정 상 가 동 -> 공백이 두칸 붙어있는 경우만 제거

# 글자 치환
print("고장".replace("고장", "fault")) # fault
print("고장".replace("고", "fault")) # fault장

# replace() 문자열 단어 치환
str8 = "설비 정상 가동"
print(str8.replace("정상", "점검")) # 설비 점검 가동
 
# replace() 체이닝
num = "    010-1234-1234    "
print(num.replace(" ","").replace("-","")) # 01012341234

# ===========================================================

# 리스트 - 여러 값을 순서대로 담는 그릇
# 대괄호 안에 값들을 쉼표로 나열 (사과,배,감) -> 사과 = 0 , 배 = 1, 감 = 2
# 번호로 조각 하나를 꺼냄(0부터,문자열과 동일)
# 왼쪽에서부터 0으로 시작하는 인덱스가 자동 생성

# split() - 정해진 구분자로 문자열을 여러 조각으로 나누기
# 슬라이싱은 위치로 자르기, split은 구분자로 나누기
"에스프레소 아메리카노 카페라떼".split()
drinks = "에스프레소 아메리카노 카페라떼" # ["에스프레소", "아메리카노", "카페라떼"]
print(drinks.split())
  # 띄어쓰기를 기준으로 나뉘어진 세 개의 문자열을 대괄호에 감싸서 반환된다
# 구분자를 특정하고 싶은 경우
fruits = "딸기,거봉,키위,사쿠란보"
print(fruits.split(",")) # ['딸기', '거봉', '키위', '사쿠란보']
  # 문자열 콤마를 기준으로 분할

# 원래는 공백이 영향을 받지만 print할때는 받지 않는다
fruits2 = "딸기, 거봉, 키위, 사쿠란보"
print(fruits2.split(",")) # ['딸기', ' 거봉', ' 키위', ' 사쿠란보']

# 리스트의 인덱스
fruits_list = fruits.split(",")
print(fruits_list) # ['딸기', '거봉', '키위', '사쿠란보']

# 거봉만 출력하기
print(fruits_list[1]) # 거봉
print(fruits_list[3]) # 사쿠란보
print(fruits_list[-1]) # 사쿠란보

# split 횟수 제한
num = "010-1234-1234"
# ["010", "1234-1234" ]
print(num.split("-", 1))

bam = "a,b,c,d"
print(bam.split(","))

# ==============================================================

# join() - 리스트의 여러 조각을 하나의 문자열로 합치기
# "구분자".join(리스트)

# fruits_list.join(",")

"-".join(fruits_list) # "딸기-거봉-키위-사쿠란보"
",".join(fruits_list) # "딸기,거봉,키위,사쿠란보"
", ".join(fruits_list) # "딸기, 거봉, 키위, 사쿠란보"

ab = ["2025","01","15"]
print("-".join(ab))


# pyThon 출력하기

word = "python"
# 방법1 )srtip + capitalize
# print(word[:2]) + word.strip("py").capitalize

# 방법2 ) replace 사용
print(word.replace("t","T"))

# 방법3 ) 슬라이싱 + T만 upper 사용
print(word[:2] + word[2].upper() + word[3:])

# 방법4 ) 인덱싱으로 글자 하나씩 연결
print(word[0] + word[1] + word[2] + word[3].upper() + word[4] + word[5])

# 방법5 ) 인덱싱 + strip + title
print(word[:2] + word.strip("py").title())

# 방법6) split + join 
print(word.split("t")) # ["py", "hon"]
print("T".join(word.split("t"))) # pyThon

# =====================================================================

# print 함수의 sep, end
print("2026", "07", "27") # 2026 07 27
print("2026", "07", "27", sep="사랑해") # 2026사랑해07사랑해27
# 공백대신에 문자열 삽입되어 이어짐

print("안녕", "하세") # 안녕 하세
print("안녕", "하세", end="요\n") #안녕 하세요
# end 속성 사용 시 출력문 마지막에 해당 문자열이 붙어 삽임

# print 함수 + 사용 시 sep과 end
print("안녕", "하세", end="요" + "이렇게?!")  #안녕 하세요안녕 하세요이렇게?

# 기본적으로 print문에는 sep으로 공백 한 칸,
# end로 |n(줄바꿈)이 적용되어 있음
# 근데 개발자가 각 속석을 직접 부여할 경우
# 기본값이 아닌 전달받은 속성값을 적용

note = "2026/07/27"
notebo = note.split("/")
print("-".join(notebo))

ttt = "1, NORMAL ,25.3"
bbb = ttt.split(",") # ['1', ' NORMAL ', '25.3']
ccc = bbb[1].strip().lower()
print(ccc) 

# =================================================================

# f-string - 문자열 안에 변수 값을 바로 끼워 넣는 출력
# f"설비{code}점검"은"설비 EQP-001 점검"
# f"{}" 형태로 변수를 중괄호로 감쌈
# 따옴표 앞 f가 중괄호를 변수로 해석하라는 신호
  # name = "홍길동"
  # age = 25
  # print(f"{name}님은 {age}살입니다")
  # code = "EQP-001"
  # print(f'설비 {code} 점검 완료')

# 출력 결과 : 설비 PUMP_A, 온도 87도
#기존방식
name = "PUMP_A"
temp = 87
print("설비 " + name + ", 온도 " + str(temp))

# f-string
print(f"설비 {name}, 온도 {temp}도")

# f-string 연산
hour = 8

# 우리는 하루에 8시간 수업을 듣고, 이는 480분입니다.
print(f"우리는 하루에 {hour}시간 수업을 듣고, 이는 {hour * 60}분입니다.")

ae = 77
ab = 23
ac = 45
print(f"평균 {(ae + ab + ac) / 3}")

hi = 87.456
print(f"{hi:.2f}")  
print(f"{hi:.3f}")

# 만들기·출력 - 따옴표, print, f-string, 형변환
# 꺼내기 - 인덱싱, 슬라이싱, split
# 확인·다듬기 - len·in·find / strip·lower·replace·join

by = " 5 , sensor_2 , Warning , 0.78912 "
bi = by.strip().split(",")
hi = bi[1].strip()
hello = bi[2].strip().lower()
hing = float(bi[3].strip())
print(f"[센서 {hi}] 상태 {hello}, 측정값 {hing:.2f}")

