# ======================실습 1 =============================
f = open("sample.txt", "r", encoding="utf-8") 

with open("sample.txt", "r", encoding="utf-8") as f:

   lines = f.readlines()

print(lines)

# 쓰기모드(write)로 파일을 새롭게 만들어 보겠습니다
f = open("sample.txt", "w", encoding="utf-8")


# 파일 쓰기에 줄바꿈을 포함하려면 \n을 포함
f.write("안녕하세요")
# 파일 쓰기에 들여쓰기를 포함하려면
f.write("\t반갑습니다")


f.close()


# ========= 실습 2 ===================================

with open("happy.txt", "w", encoding="utf-8") as f:

    # ② 파일에 내용 쓰기
    f.write("오늘은 피곤한 하루입니다.\n")
    f.write("파이썬 입니다.")

# ③ with 블록이 끝나면 파일이 자동으로 닫힘


# ④ happy.txt 파일을 읽기 모드로 다시 열기
with open("happy.txt", "r", encoding="utf-8") as f:
    aa = f.read()

print(aa)