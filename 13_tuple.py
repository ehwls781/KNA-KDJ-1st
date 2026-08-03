# tuple : 값을 묶어주는 역할
# () 소괄호 안에 쉼표로 나누어서 여러가지 자료형의 값을 저장
# 마지막 값에는 꼭 ,를 붙여야 튜플로 인식
# 짝지어진 값을 하나로 묶을 때 사용 가능한 자료형

sensor = ("모터온도", 78)
print("sensor", sensor) # sensor ('모터온도', 78)
print("type(sensor): ", type(sensor)) # type(sensor):  <class 'tuple'>

# tuple이 되는 조건 ?
# 쉼표 + 괄호 = tuple
# ()가 있으면 tuple? -> x
  # 요소 갯수 확인하기
# 요소 갯수
# 요소 2개 이상: 쉼표가 있다면 tuple
# 요소 1개: 쉼표
# 요소 0게(빈 튜플): () 빈 괄호

# tuple 에서 많이 헷갈려하는 부분
# (1, 2) -> tuple
# (1): int <- int만 있어서 int
# (1,): tuple <- 괄호 + , 
# (1, 2, 3,) <- 가장 마지막에 쉼표를 붙여서 tuple임을 명시
# (1, 2, 3) <- tuple
num_tuple = (
  1,
  2,
  3,
)
# tuple

# tuple의 인덱스
print(sensor[0]) # 모터온도

# 튜플의 슬라이싱
s = ("a",
     "b",
     "c", 
     "d", 
     "e",
)
print(s[1:4]) # ('b', 'c', 'd')
print(type(s[1:4])) # <class 'tuple'>

# tuple unpacking
# 튜플에 담긴 값을 변수로 한 번에 분리

# 복습) 복수의 변수 한 번에 선언
a, b, c = "a", "b", "c"
print(a) # 문자열 a
print(b) # 문자열 b
print(c) # 문자열 c

unpacking = (
  1, # 변수 one
  2, # 변수 two
  3, # 변수 three
)

# unpacking = one, two, three 
# one, two, three라는 알 수 없는 변수를
# unpacking 변수에 할당하겠다는 의미
# 동작 x

# one, two, three = unpacking
# unpacking이라는 변수에 담긴 튜플
# 할당 연산자 왼쪽 one, two, three
# 풀어서 담는다는 뜻
# print("one", one)
# print("two", two)
# print("therr", three)

# 튜플의 언패킹은 변수의 개수와
# 튜플에 담긴 값의 개수가 동일해야 함

# 리스트 언패킹이 가능할까?
one, two, three, four = [1, 2, 3, 4]
print("one: ", one)
print("two: ", two)
print("therr:", three)
print("four:", four)
# 가능하다

# ========================================================================

tup = ("normal", "normal", "warning", "normal", "worning",)

# 튜플의 길이
print(len(tup)) # 5

# 특정값의 갯수 새기
print(tup.count("warning")) # 2

# 특정 값의 처음 위치 찾기
print(tup.index("warning")) # 2
  # 찾고자 하는 값이 없으면 Error발생

# =====================================================================

# 튜플 리스트
# 리스트 안에 복수의 튜플을 담는 것
# for문으로 리스트를 사용해서 리스트 내부의 튜플에 접근
# 튜플에 담긴 값을 사용할 수 있음

# 언패킹을 사용해서 접근한 튜플 내부의 값을 
# 변수에 바로 할당해서 접근

hour_13 = [("모터온도", 77), ("모터진동", 0.2), ("모터압력", 91)]
now = 0

for name, value in hour_13:
  now += 1
  print(now, "번째 반복")
  print("name:", name, "value:", value)

# =====================================================================

temps_13 = [("qox_001", 81), ("qox_002", 88), ("qox_003", 95), ("qox_004", 89),]

Warning = 90

for name,temp in temps_13:
  if temp >= Warning:
    print(name, "경고")

# 리스트 안의 튜블 갯수가 늘어나면 
# for문에서 변수를 여러 개 작성하면 된다

tup_list = [("일", "one", 1, "1"),
            ("이", "two", 2, "2"),
]

# for문에서도 언패킹 할 때는 무조건 
# 튜플의 값 개수와
# for문의 변수 갯수 통일
# 통일하지 않으면 Error 발생

# for kor_str, eng_str, num, num_str in tup_list:
#   print("kor_str:"kor_str,
#         "eng_str:"eng_str, 
#         "num:"num,
#         "num_str:"num_str)
  
# ====================================================

# 튜플 리스트 정렬

# sorted()를 사용하여 튜플의 특정 값 기준으로
# 리스트를 정렬

temps_13 = [(81,"qox_001"),
            (88,"qox_002"),
            (95,"qox_003"),
            (89,"qox_004"),]

# sorte()는 원본 배열을 수정하지 않고
# 새 리스트를 반환
hot = sorted(temps_13, reverse=True)
print(hot) 

a = ("온도", 78)
print(a)
print(a[0])
name, value = a
print(name, value)

b = [("모터1", 91), ("모터2", 77), ("모터3", 78)]

Warning = 90

for name, temp in b:
  if temp >= Warning:
    print("경고")

sensors = [
("모터온도", 78, (3, 5)),
("베어링진동", 0.5, (7, 2)),
("펌프압력", 95, (4, 8)),
]
for name, value, pos in sensors:
  x, y = pos
  print(name, "위치:", x, y)
for name, value, pos in sensors:
  x, y = pos
  if x <= 5:
   print(name, "1구역")