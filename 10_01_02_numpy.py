# 파이썬에서 기본 제공하는 기능들 외에
# 다양한 외부 라이브러리를 가져오려면
# pypi.org 사이트에서 검색하기

# 터미널에서 바로 pip로 설치를 시도하면
# 전체 시스템에 영향을 주는 선치로 생각되어
# 거절당한다
# 개별 working directory마다 별도의 환경을 구축해
# 그 안에 개별 프로젝트가 사용할 pip 라이브러리를 받아 쓴다
# 이것이 바로 가상환경

# 1. 현재 경로에 가상환경 생성
# python -m venv .venv

# 2. 가산황경 활성화
# source .venv/Scripts/activate
# (이후에는 가상환경 안에서 터미널 명령 실행 가능)
# 예시 ) pip install numpy

# 3. (작업/실행끝나고) 가상환경 종료
# deactivate

import numpy as np

numbers = [1,2,3,4,5]
# 위 int값들의 리스트를 사용해서 numpy의 배열 만들기
np_numbers = np.ndarray(numbers)
print(np_numbers)