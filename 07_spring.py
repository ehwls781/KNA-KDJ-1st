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