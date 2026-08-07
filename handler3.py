# # 실습 1

# # ① open으로 파일을 읽기 모드 r, utf-8로 열기
# f = open("practice_1.txt", "r", encoding="utf-8")
# # ② read로 전체를 한 문자열로 읽어 출력
# read_txt = f.read()
# print(f"read로 출력: {read_txt}")
# f.close()
# # ③ readlines로 줄 리스트로 읽어 출력
# with open("practice_1.txt", "r", encoding="utf-8") as f:
#     readlines_txt = f.readlines()
# print(f"readlines로 출력: {readlines_txt}")

# 실습 2 
origin = input("온도 : ")

print(f"입력한 온도: {origin}")

try:
    temp = int(origin)
except ValueError:
    # ValuError인 상황이었다면 여기로 예외
    print("숫자 아니면 왜 불렀어요? 0으로 생각할래")
except TypeError:
    # TypeError인 상황이었다면 여기로 예외
    print("타입 문제는 전지구적 문제입니다")
    temp = 0

next_temp = temp + 10
print(f"10도만 더 높으면 {next_temp}")

# 실습 4

import csv
import os

csv_path = os.path.join("KNA-KDJ-1st", "실습파일.csv")

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)

# 실습 5 - 파일 만들기

import csv

csv_path = "실습파일.csv"

with open(csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["시각", "설비"])
    writer.writerow(["15:00", "PUMP-04"])
    writer.writerow(["16:00", "MOTOR-01"])