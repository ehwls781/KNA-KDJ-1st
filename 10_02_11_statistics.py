import numpy as np

# 합계(sum)와 평균(mean)
s = np.array([70, 82, 71, 95, 73])
print(s.sum()) # 391
print(s.mean()) # 78.2
print(np.median(s)) # 73.0

# 최대/최소 범위
print(s.max()) # 최댓값 95
print(s.min()) # 최솟값 70
print(s.max() - s.min()) # 범위 25

# 분산코드
stable = np.array([70, 71, 70, 72, 71])
unstable = np.array([60, 85, 65, 95, 70])
print(stable.var()) # 0.5599999999999999
print(round(stable.var(), 2)) # 0.56

print(unstable.var()) # 170.0
print(round(unstable.var(), 2)) # 170.0

# 표준편차(std)
s2 = np.array([70, 72, 71, 95, 73])
print(round(s2.var(), 2)) # 분산 89.36
print(round(s2.std(), 2)) # 표준편차 9.45