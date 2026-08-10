# 미국식 속도 miles를 
# 우리가 쓴느 속도 km로 변환
# 시키는 Numpy 배열 예시코드

import numpy as np

miles = np.array([94.7, 104.5, 105.5])
# 속도 = 속도 * 1.60934

print(miles * 1.60934)
# (152.404498 168.17603 )
