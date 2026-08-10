import numpy as np

# linspace
# 개수 중심 균등 분할
# 시작과 끝 구간을 지정한 개수만큼 나누기

# 0부터 1까지 5개로 균등 분할
div_five = np.linspace(0, 1, 5)
print(div_five) # [0.   0.25 0.5  0.75 1.  ]