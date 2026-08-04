# dictionary - 순서 번호 대신 이름표로
# 값을 바로 찾는 자료구조

# 리스트로 크루 여러분의 이름을 나열
data_class = ["태구", "수진", "영준"]

# 딕셔너리로 정확하게 역할 부여
data_class_dict = {"반장": "태구"
                   , "부반장": "수진"
                   , "당번": "영주"}

# 센서로 부터 얻는 예시 데이터로
# 딕셔너리를 만들어봅시다

sensors = { "센서이름": "보일러", 
           "모터온도": 78,
           "진동": 0.5 }

print(sensors)
print(type(sensors)) # <class 'dict'>
empty = {} # 빈 딕셔너리
print(type(empty)) # <class 'dict'>

print(sensors["모터온도"])
print(sensors["진동"])

# 기존에 있던 key의 값을 변경
sensors["센서이름"] = "펌프" # 센서이름 변경
sensors["진동"] = 0.7 # 진동 값 변경

# 더 이상 필요없는 key와 그 value를 삭제
del sensors["모터온도"]

# 기존에 없던 key의 값을 추가
sensors["펌프입력"] = 95
print(sensors)

# print(sensors["모터온도"]) # KeyError 발생

print(sensors.get("센서이름")) 

motor_degree = sensors.get("모터온도", 0)
next_degree = motor_degree + 10

# is_motor_degree_key = "모터온도" in sensors
# print(is_motor_degree_key)

# if is_motor_degree_key:
#   print("그런 키 있어요")
# else:
#   print("그런 키 없어요")

# 위 코드는 이렇게 쓰인다

if "모터온도" in sensors:
  print("그런 키 있어요")
else:
  print("그런 키 없어요")

# keys를 가져오기 
print(sensors.keys())
print(sensors.values())
# len을 통해 몇개의 key-value 조합들이 있는지 확인
print(len(sensors)) # 답 : 3

for key, value in sensors.items():
  print(key)
  print(value)

# 조금더 많이 사용하는 코드
for name, value in sensors.items():
  print(name)
  print(value)

if len(sensors) < 5:
  print("내용이 부족해요")

# 재미난 사례 만들기
# 나라 이름으로 정리
# 유럽 : 스페인, 프랑스, 독일, 스위스, 네덜란드
# 아시아 : 한국, 일본, 중국, 사우디, 이란
# 남미 : 아르헨티나, 브라질, 칠레, 콜롬비아, 우루과이
# 각 나라마다 이름과 약칭으로 정리가능

korea = {"국가명": "대한민국", "약칭": "KOR"}
japan = {"국가명": "일본", "약칭" : "JPN"}

# 아시아 나라들을 하나의 리스트로 모으기

asia = [korea, japan]
print(asia)

# 유럽 나라들을 하나의 리스트로 모으기

europe = {"국가명": "스페인", "약칭": "SPA"},
{"국가명": "프랑스", "약칭": "PRA"},
{"국가명": "스위스", "약칭": ""},
{"국가명": "네덜란드", "약칭": "KOR"},
{"국가명": "독일", "약칭": "KOR"}

for country in europe:
   print(country.get("국가명"))
   for key, value in country.items():
      print(f"{key}:{value}")

  

# 조별과제
# 포켓몬 1,2,3 진화단계들을 딕셔너리로 만들고
# 그 포켓몬 딕셔너리들이 모인 배열 만들기
# 배열 데이터를 화면에 프린트
# 가능하면 배열의 데이터들을 for~in 사용해서 꺼내 프린트하기

pocket_mon = [
    {"1단계": "꼬부기", "2단계": "어니부기", "3단계": "거북왕"},
    {"1단계": "이상해씨", "2단계": "이상해풀", "3단계": "이상해꽃"},
    {"1단계": "파이리", "2단계": "리자드", "3단계": "리자몽"},
    {"1단계": "피츄", "2단계": "피카츄", "3단계": "라이츄"},
    {"1단계": "캐터피", "2단계": "단데기", "3단계": "버터플"},
    {"1단계": "뿔충이", "2단계": "딱충이", "3단계": "독침붕"},
    {"1단계": "구구", "2단계": "피죤", "3단계": "피죤투"},
    {"1단계": "알통몬", "2단계": "근육몬", "3단계": "괴력몬"},
    {"1단계": "고오스", "2단계": "고우스트", "3단계": "팬텀"},
    {"1단계": "케이시", "2단계": "윤겔라", "3단계": "후딘"},
]

print(f"포켓몬 종류 : {pocket_mon}")

for dic in pocket_mon:
    for name, value in dic.items():
        print(f"포켓몬 진화 단계 : {name}, 포켓몬 이름 : {value}")

# 다음의 두 딕셔너리는 같은 key를 가지고 있다
# 실제 데이터
values = { "모터온도": 95, "압력": 88 }
# 임계치 데이터
limits = { "모터온도": 90, "압력": 90 }

for name, value in values.items():
   print(f"{name} : {value}")

   # limits 딕셔너리에도 name의 key가 있다면
   # 가져와서 비교하기
   if value > limits.get(name, 0):
      print(name, "경고")

sensors = {"모터온도": 78, "진동": 0.5}
cons = {"모터온도": 88, " 유량": 42}
sensors.update(cons)
print(sensors)

# zip으로 key들의 배열과
# value들의 배열을 묶어서
# 새로운 딕셔너리 만들기

names = ["모터온도", "진동", "입력"]
values = [78, 0.5, 95]
sensors = dict(zip(names, values))
# zip 기능으로 두 배열을 사용해 묶고
# dict 타입 딕셔너리로 만들기
print(sensors)

# 딕셔너리 안에 value로 list도 가능
idols = {
   "BTS" : ["RM", "진", "슈가", "제이홉", "지민", "뷔", "정국"],
   "블랙핑크" : ["지수", "제니", "로제", "리사"],
   "뉴진스" : ["민지", "하니", "다니엘", "해린", "혜인"]}

my_classroom = {
   "학년": 3,
   "반": 1,
   "반장": "홍길동",
   "부반장": ["고길동", "둘리"]
}

# 딕셔너리 안에 value로 딕셔너리를 사용하기
kbo = [
      {
   "구단명": "삼성",
   "마스코트": "라이온스",
   "구장": "대구"
},
{
   "구단명": "두산",
   "마스코트": "베어스",
   "구장": "잠실"
}]

# 쉽게 배열 안에 딕셔너리 안에 딕셔너리 접근
print(kbo[0]["구장"])

# ==============================================

# 실습 1. 딕셔너리 만들고 다루기

# 1) 센서명을 키(key)
# 측정값을 (value)로 딕셔너리 저장

sensors = {"모터온도": 78,
           "진동": 0.5}

# 2) 키로 값을 꺼내고 새 키로 추가
# 기존 키로 수정
print(sensors["진동"]) # 값 꺼내기
print(sensors.get("진동", 0)) # 안전하게 값 꺼내기

sensors["압력"] = 95 # 추가
sensors["진동"] = 0.3 # 있던 키 언급하면 수정

print(sensors)

# 3) get으로 없는 키를 기본값으로 조회
# in으로 키 존재 확인
print(sensors.get("면적", -1))
# 면적 key는 존재하지 않아 -1로 대체
print("진동" in sensors) # 존재하는 key
print("면적" in sensors) # 존재하지 않는 key

# 실습 2. update로 여러 값 한 번에 갱신
mouse = {"피곤함 수치": 90}
phone = {"배고픔 수치": 70}

mouse.update(phone)
print(len(mouse)) # 2
del(mouse["피곤함 수치"])
print(len(mouse)) # 1

# 실습 4.zip로 센서명-값 매핑하기

name = ["온도", "진동", "압력"]
value = [74, 0.7, 100]

sensor = dict(zip(name, value))
print(sensor)
for a, b in sensor.items():
    print(a, "-", b)

# 실습 7. 표 데이터를 딕셔너리로 변환

rows = [
    "온도,74",
    "진동,0.7",
    "압력,100"
]
sensor = {}

for row in rows:
    name, value = row.split(",")
    sensor[name] = float(value)
print(sensor)

# 간단한 딕셔너리 예제
location_dict = {
   "시": [{
      "이름" : "서울특별시",
      "기초단체" : ["종로구", "중구", "마포구"]

       # 대구광역시
       # 부산광역시
   }
   ] ,
   "도":[
     {
        "이름" : "경기도",
        "기초단체" : [ "수원시", "안양시", "안산시"
                   ] 
     } 
     # 경상북도

   ]
}

# 전체출력
print(location_dict)
print("===================================")

# 시와 도 단위 딕셔너리 들을 각각 출력

print(location_dict("시"))
print(location_dict.get("도"))

# 각 시 도 마다 세부 딕셔너리들을 출력

for basic_dict in location_dict["시"]:
   print(basic_dict.get("이름"))
   print(basic_dict.get("기초단체"))


for basic_dict in location_dict("시"):
   print(basic_dict.get("이름"))
   print(basic_dict.get("기초단체"))

# 위 두 코드는 똑같은 행동을 하기 떄문에
# 중복은 묶고 효율성을 더 올리기위해
# Function 이라는 함수를 사용한다
