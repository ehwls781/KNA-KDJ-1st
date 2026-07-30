# 기존 배열의 모든 요소에 3을 곱한 값을 가진 새 리스트 생성
temps = [1, 5, 2, 7, 4, 8, 10, 3]
doubled = []

for t in temps:
  doubled.append(t * 3)

print(doubled)

# 조건에 맞는 값으로 새 리스트 만들기

# temps = [1, 5, 2, 7, 4, 8, 10, 3]
hingh = []
low = []

for t in temps:
  if t < 5:
    low.append(t)
  else:
    hingh.append(t)

print("high", hingh)
print("low: ", low)

temps = [25, 32, 28, 35, 27, 31, 24, 33]
hot = []
for t in temps:
 if t > 30:
  hot.append(t)
print(hot) # [32, 35, 31, 33]
print(len(hot)) # 4

temps = [22, 25, 32, 26, 27]
fahrenheit = []
for t in temps:
 fahrenheit.append(t * 1.8 + 32)
print(fahrenheit)

# ==========================================

# 리스트 안의 리스트
rows = [["펌프", 25], ["모터", 32], ["압축기", 28]]
# 표(행, 열)처럼 한 줄에 여러 값이 묶인 데이터
# 바깥 대괄호를 "행", 안쪽 인덱스 리스트를 "열"

print(rows[0]) # ['펌프', 25]
print(type(rows[0])) # <class 'list'>
print(type(rows)) # <class 'list'>
# 중첩된 리스트 안의 값에 접근
print(rows[1])
# 1. rows[1]을 찾음 -> ['모터', 32]
print(rows[1][1])
# 2. print(["모터", 32]) -> [1] 앞의 리스트에서 1번 인덱스 값에 할당
# 3. print(32) -> 32출력

# 출력된 리스트 내부의 값은 대괄호를 여러번 이어서 접근

# 리스트 안의 리스트 온도값만 출력하기
for row in rows:
  print(row[0], "온도", row[1]) # 펌프 온도 25 ...
# rows는 리스트를 담고 있는 큰 리스트
# row는 rows 안에 있는 작은 리스트 예) ["펌프", 25] 하나

a = [22, 31, 35, 27, 40, 29, 33, 24]
b = 0
c = []

for i in a:
    b = b + i

    if i > 30:
        c.append(i)
d = 0
for i in c:
    d = d + i
print("전체 평균:", b / len(a))
print("고온 개수:", len(c))
print("고온 평균:", d / len(c))
