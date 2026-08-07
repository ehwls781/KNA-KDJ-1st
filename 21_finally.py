# except 연속사용과 finally 코드

# text = "24.5" # 정상
text = "영크크" # 비정상

temp = 0
try:
  temp = float(text)

except ValueError:
  print("ValueError 발생!")
  
except NameError:
  print("NameError 발생")
finally:
  # 오류가 있건 없건 finally의 코드를
  # 실행하고 마무리한다
  print(temp * 2) # 

# ===== 실습 1 ====
try:
    f = open("sample.txt", "r", encoding="utf-8")
    print(f.read())

finally:
    f.close()

# === with open 사용해서 더 안전하게

name = 0
with open(name) as f:
   data = f.readlines()

