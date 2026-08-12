# 실습 1. CSV 불러오기 워밍업

import pandas as pd
import os

filepath = os.path.join("KNA-KDJ-1st" "12_metro_small.csv") # "data/12_metro_small.csv"

try:
    df = pd.read_csv(filepath, encoding="utf-8", sep=",", index_col="측정시각", nrows=5, usecols=["측정시각", "가동상태"])
    print(df.shape) # (30, 7)

    print(df.head(10))
except FileNotFoundError:
    print(f"파일이 없습니다 : {filepath}")

# 실습 2 =====================================================
# 실습2 / 설비 센서 CSV 불러오기
# GOAL read_csv로 데이터를 불러와 head로 확인
# 실습 과제

import pandas as pd
# import os

# # 12_metro_compressor.csv
# # 200행 7열 — 인덱스 3번 행 오일온도가 NaN

# file_path = os.path.join("data", "12_metro_compressor.csv")

# df = pd.read_csv("data/12_metro_compressor.csv", encoding='utf-8')
# print(df.head(10))
# print(df.shape)

# STEP 1
# import 후 read_csv로 담고 head로 확인

# 실습 3=======================================================

# 세미콜론 구분 파일
# sep 없이 읽으면 200행 1열, sep=";"이면 200행 7열

import pandas as pd

df = pd.read_csv("KNA-KDJ-1st/12_metro_compressor.csv", sep=";", encoding="utf-8")
print(df.shape) # (200, 7)
print(df.head(4))

# 실습 4 =======================================================

# 필요한 열만 골라오기

import pandas as pd

df = pd.read_csv("KNA-KDJ-1st/12_metro_compressor.csv",
                 usecols=["측정시각", "오일온도", "모터전류"])
print(df.shape) # 200, 7 - > (200, 3)
print(df.head(3))

# 실습 5 ===========================================================

# 경로 옵션 오류 고치기
# 오류 메시지 읽고 스스로 원인 찾아가서 고치기

import pandas as pd

# 오류 코드
# df = pd.read_csv('아무거나주세요.csv', encoding="utf-8")
# print(df.shape) # FileNotFoundError: [Errno 2] No such file or directory: '아무거나주세요.csv'

# df = pd.read_csv("data/12_metro_compressor.csv", encoding="utf-8")
# print(df.shape) # (200, 7)

# 실습 6 ============================================
# 세미콜론 + 한글 파일에서 필요한 열만 꺼내기
# 여러 옵션을 함께 써서 shape 확인
# encoding 도 지정하기

# 실습 1 . head-tail로 데이터 열기 =========================================

import pandas as pd

df = pd.read_csv("KNA-KDJ-1st/12_metro_digital.csv")
print(df.shape)
print(df.head())
print(df.tail())

# 실습 2  head, tali 행 개수 조절 =========================================
import pandas as pd

df = pd.read_csv("KNA-KDJ-1st/12_metro_digital.csv")
print(df.shape)
print(df.head(3))
print(df.tail(7))

# 실습 3 구조 파악 3종 도구 ===========================================
# shape columns dtype 로 데이터 뼈대 읽기

# 12_metro_digital.csv 읽어와서 DataFrame에 담기
# .shape 출력
# .coulumns 출력
# .dtypes 출력
# df.columns.tolist() 도 출력

import pandas as pd

# CSV 파일 읽기
df = pd.read_csv("KNA-KDJ-1st/12_metro_digital.csv")

print(df.shape)

print(df.columns)

print(df.dtypes)

print(df.columns.tolist())

# 실습 4 열 이름 자료형 점검 =======================================

# 12_metro_compressor.csv 읽어와서 DF에 담기
# .culumns 출력 df.columns.tolist() 도 출력
# DF의 dtypes 출력

import pandas as pd

df = pd.read_csv("KNA-KDJ-1st/12_metro_compressor.csv")

print(df.shape)
print(df.columns)
print(df.columns.tolist())

# 실습 5. info로 데이터 건강검진 ===================================

import pandas as pd

df = pd.read_csv("KNA-KDJ-1st/12_metro_digital.csv")
df.info()