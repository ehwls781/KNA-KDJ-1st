import numpy as np

# 0으로 채우기
block_zeros = np.zeros(5)
print(block_zeros) # [0. 0. 0. 0. 0.]

# 7로 채우기
block_seven = np.full(4, 7) # 0을 마지막에 넣으면 출력값에 소수점이 생긴다
print(block_seven) # [7 7 7 7]
  