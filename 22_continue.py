# 반복문 안에서 예외처리

my_list = ["123","456","영크크","32","53"]

for text in my_list:
  # 반복을 하는 중에 문제가 생긴 경우만 건너뛰고
  # 계속 반복을 이어서 진행시키기
  try:
    my_number = int(text)
  except:
    print("문제발생")
    # 문제가 생겼다면 더 이상 반복문 안의 출력까지 이어가면 안되겠다
    # 그래서 여기서 끊고 다음 내용 처리하게 반복문 넘기기

    # 갈 때 가더라도 문제상황
    # problem += 1

    continue

  print(my_number)

# 실습 2 견고한 예외처리 - 불량줄 건너뛰기
# 소숫점 이하의 숫자가 포함된 숫자들을 
# 20개정도 만들어 배열
# 그 사이에 엉뚱항 글자들이 포함된 내용도 포함시키기
# 위 리스트 데이터를 사용해 풀어보기
note_book = ["20.1", " abc", "21.1", " cxs", " 22.2"," 30.0",
"11.3","12.3","15.4"]

for i in note_book:
    try:
        print(float(i))
    except ValueError:
        continue
    
# 실습 3 여러파일 묶어 처리하기
# 다음과 같은 식의 리스트를 만들어 반복문으로 철
# for문으로 리스트의 문자열을 꺼내 해당 이름의 파일들을 여보기

file_names = ["08_press.csv","실습파일.csv"]

for file in file_names:
    try:
        f = open(file, "r", encoding="utf-8")
        print(file, "열기 성공")
        f.close()

    except FileNotFoundError:
        print(file, "파일이 없습니다.")

# 실습 4 잘못된 함수 만들고 확인

def check_age(age):
    try:
        age = int(age)

        if age < 0 or age > 120:
            print("잘못된 나이입니다.")
        else:
            print("나이:", age)

    except ValueError:
        print("숫자를 입력해주세요.")

check_age("24")
check_age("abc")
