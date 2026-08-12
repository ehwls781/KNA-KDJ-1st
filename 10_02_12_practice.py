import numpy as np

# 실습 6. 센서별 기초 통계 구하기
# 2차원 표 데이터에서 통계






# ====================================

# 실습 7. 파일 데이터로 기초 통계 구하기
# 파일로 저장된 공정 데이터를 불러와 기초 통계 계산

# np.loadtxt로 회전수 열을 파일에서 불러오기
rpm7 = np.loadtxt("KNA-KDJ-1st/10_mct_tool.csv", delimiter = ",", skiprows=1, usecols=4, encoding="utf-8")
# 불러온 배열의 평균과 표준편차 계산
print(round(rpm7.mean(), 1)) # 4212.6
# 최솟값과 최댓값으로 값의 범위 확인

# 예상 결과
# 회전수의 평균-표준편차와 최솟값-최댒값이 출력

# ==============================================================

# 실습 8. 필터링과 통계 결합하기
# 조건으로 값을 골라낸 뒤 그 값들의 통계 계산

# 토크배열 준비
torque8 = np.array([42.8, 46.3 ,49.4, 65.7, 41.9])
# 불리언 인덱싱으로 기준을 넘는 값만 추출
high8 = torque8[torque8 > 50]
print(high8) # [65.7]
# 추출한 값들의 평균과 개수 계산
print(round(high8.mean(), 1)) # 65.7
# 예상결과
# 기준 초과 값들의 평균과 개수가 출력

# ===================================================================

# 실습 9. numpy 기조 종합 분석
# 데이터 불러오기, 구조 확인, 필터링
data9 = np.loadtxt("KNA-KDJ-1st/10_mct_tool.csv", delimiter = ",", skiprows=1, usecols=(4,5), encoding="utf-8")
print(data9)

# shape과 dtype으로 구조 확인
print(data9.shape, data9.dtype) # (40, 2) float64
# 회전수가 기준 아래로 떨어진 이상 시점을 필터링해 개수와 평균 계산
rpm9 = data9[:, 0]
print(rpm9)
anomaly = rpm9[rpm9 < 1000]
print(anomaly) # [58.]
print(anomaly.size, round(anomaly.mean(), 1)) # 1 58.0

# 예상 결과
# 데이터 구조