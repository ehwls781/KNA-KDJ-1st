import numpy as np

# 파이썬의 리스트로부터 Numpy 배열 만들기
temp = np.array([70.5, 69.9, 73.6])

print(temp) 

# 배열의 항목들마다 +5씩 더하려면
# 리스트였따면 for문으로 돌려서 항목마다 직적ㅂ처리했어야함
# numpy라면 간단하게
print(temp + 5)

