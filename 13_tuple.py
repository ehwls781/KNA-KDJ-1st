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