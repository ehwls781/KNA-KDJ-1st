# 실습 1번

# (설비명, 온도, 진동)

# 판정 기준
#   온도 > 90 또는 진동 > 5.0  > "위험"
#   온도 >= 80 또는 진동 >= 3.0 > "주의"
#   그 외                      > "정상"

# TODO 1. 각 설비 상태 판정해서 번호 붙여 한 줄씩 출력 (for + enumerate + if/elif/else)


# TODO 2. 정상 / 주의 / 위험 각각 몇 대인지 세서 출력 (누적변수)


# TODO 3. 이상 설비(주의 + 위험) 비율 % 출력 (round)


# TODO 4. 전체 평균 온도 출력 (round)


# TODO 5. 온도 가장 높은 설비 이름 + 온도 출력 (반복문으로 직접 찾기)


# TODO 6. "위험" 설비 이름만 모아서 정렬해 리스트로 출력 (.append() + .sort())


# 도전) 위험 1대라도 있으면 "⚠ 즉시 점검 요망", 없으면 "✅ 전 설비 안정"

# ========================================
#         설비 종합 모니터링 리포트
# ========================================
# 1. 컨베이어_01 | 온도 78℃ | 진동 2.1mm/s | 정상 ✅
# 2. 용접기_02 | 온도 92℃ | 진동 5.4mm/s | 위험 🚨
# ...
# ----------------------------------------
# 총 설비: 7대
# 정상: 2 / 주의: 3 / 위험: 2
# 이상 설비 비율: 71.4%
# 평균 온도: 85.9℃
# 최고 온도 설비: 건조로_04 (101℃)
# 위험 설비 목록: ['건조로_04', '용접기_02']
# ========================================

sensors = [
    ("컨베이어_01", 78, 2.1),
    ("용접기_02", 92, 5.4),
    ("절단기_03", 85, 3.2),
    ("건조로_04", 101, 6.8),
    ("냉각탑_05", 67, 1.5),
    ("도장부스_06", 88, 4.1),
    ("성형기_07", 90, 2.9),
]
danger = 0
caution = 0
normal = 0
total_temp = 0
danger_list = []
highest_temp = 0


print("========================================")
print("\t설비 종합 모니터링 리포트\t")
print("========================================")
for idx, value in enumerate(sensors):
    if value[1] > highest_temp:
        highest_temp = value[1]
        highest_name = value[0]
    if value[1] > 90 or value[2] > 5.0:
        print(f"{idx+1}. {value[0]} | 온도 {value[1]}℃ | 진동 {value[2]}mm/s | 위험 🚨")
        danger_list.append(value[0])
        danger += 1
        total_temp += value[1]
    elif value[1] >= 80 or value[2] >= 3.0:
        print(f"{idx+1}. {value[0]} | 온도 {value[1]}℃ | 진동 {value[2]}mm/s | 주의 ⚠️")
        caution += 1
        total_temp += value[1]
    else:
        print(f"{idx+1}. {value[0]} | 온도 {value[1]}℃ | 진동 {value[2]}mm/s | 정상 ✅")
        normal += 1
        total_temp += value[1]
print("----------------------------------------")
print(f"총 설비 : {len(sensors)}")
print(f"정상: {normal} / 주의: {caution} / 위험: {danger}")
print(f"이상 설비 비율: {round((danger+caution)/len(sensors)*100, 1)}%")
print(f"평균 온도: {round(total_temp/len(sensors), 1)}℃")
print(f"최고 온도 설비: {highest_name} ({highest_temp})℃")
print(f"위험 설비 목록: {sorted(danger_list)}")
print("========================================")

# =====================================================================
# 종합 실습 2. 실시간 측정값 입력 시스템
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

# === 실시간 측정값 입력 시스템 ===
# 측정값을 입력하세요. 종료하려면 q 입력.
# 측정값: 85
# 측정값: 120
#   🚨 임계값(100) 초과! 현재까지 초과 1회
# 측정값: 60
# 측정값: q
# ----------------------------------------
# 총 입력 개수: 3개
# 최댓값: 120.0 / 최솟값: 60.0
# 평균값: 88.33
# 임계값 초과 개수: 1개
# 평균 초과 개수: 1개
# 상위 3개 값: [120.0, 85.0, 60.0]

# 이 실습은 사용자한테 입력받는 거라 미리 주는 데이터 없음
# while로 계속 입력받다가 q 입력하면 종료 > 통계 출력

print("=== 실시간 측정값 입력 시스템 ===")

LIMIT = 100  # 임계값 (100 초과 시 즉시 경고)
empty_list = []
LIMIT_TIME = 0
total = 0
big_avg = 0
big_list = []


# TODO 1. while로 "측정값: " 계속 입력받기, q면 break
#         (입력값은 숫자 아니면 q 라고 가정)
#         값은 리스트에 .append() 로 모으기
while True:
    user_input = input("측정값: ")
    if user_input == "q":
        break
    # 도전) q 대신 그냥 Enter(빈 입력 "") 치면 무시하고 다시 받기
    elif user_input == "":
        continue
    else:
        empty_list.append(float(user_input))

    # TODO 2. 입력값이 LIMIT 초과하면 즉시 경고 + 지금까지 초과 횟수 출력
    if int(user_input) > LIMIT:
        LIMIT_TIME += 1
        print(f" 🚨 임계값(100) 초과! 현재까지 초과 {LIMIT_TIME}회")


# TODO 3. q로 끝난 뒤:
#   - 입력값이 하나도 없으면 "입력된 측정값이 없습니다." 출력하고 끝
#   - 값이 있으면 아래 출력
#       · 총 입력 개수 (len)
#       · 최댓값 / 최솟값 (반복문으로 직접 찾기)
#       · 평균값 (round, 소수 둘째 자리)
#       · 임계값 초과 개수
#       · 평균보다 큰 값의 개수  > 평균 먼저 구한 뒤 리스트 다시 돌기
#       · 상위 3개 값 (.sort(reverse=True) 후 슬라이싱 [:3])
if len(empty_list) == 0:
    print("입력된 측정값이 없습니다.")
else:
    sorted_list = sorted(empty_list, reverse=True)
    # ----------------------------------------
    print("----------------------------------------")
    # 총 입력 개수: 3개
    print(f"총 입력 개수: {len(sorted_list)}개")
    # 최댓값: 120.0 / 최솟값: 60.0
    # print(f"최댓값: {sorted_list[0]} / 최솟값: {sorted_list[-1]}"

    for i in range(len(empty_list)):
        if i == 0:
            max_num = empty_list[0]
            min_num = empty_list[0]
        else:
            if empty_list[i] >= max_num:
                max_num = empty_list[i]
            elif empty_list[i] < min_num:
                min_num = empty_list[i]
    print(f"최댓값: {max_num} / 최솟값: {min_num}")
    # 평균값: 88.33
    for i in range(len(sorted_list)):
        total += sorted_list[i]
    print(f"평균값: {round(total/len(sorted_list), 2)}")
    # 임계값 초과 개수: 1개
    print(f"임계값 초과 개수: {LIMIT_TIME}개")
    # 평균 초과 개수: 1개
    for i in range(len(sorted_list)):
        if sorted_list[i] > round(total / len(sorted_list), 2):
            big_avg += 1
    print(f"평균 초과 개수: {big_avg}개")
    # 상위 3개 값: [120.0, 85.0, 60.0]
    for i in range(3):
        big_list.append(sorted_list[i])
    print(f"상위 3개 값: {big_list}")

# =====================================================================
# 종합 실습 3. 교대조 센서 경고 로그 분석
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

# === 교대조 센서 경고 로그 분석 ===
# 오전조 고유 센서 4종: ['TZ_11', 'TZ_13', 'TZ_15', 'TZ_17']
# 오후조 고유 센서 4종: ['TZ_13', 'TZ_15', 'TZ_19', 'TZ_21']
# ----------------------------------------
# 양 교대조 공통 경고 센서: ['TZ_13', 'TZ_15']
# 오전조 전용: ['TZ_11', 'TZ_17']
# 오후조 전용: ['TZ_19', 'TZ_21']
# 전체 경고 센서 6종: ['TZ_11', 'TZ_13', 'TZ_15', 'TZ_17', 'TZ_19', 'TZ_21']
# ----------------------------------------
# 경고 발생 횟수 순위:
#   1위: TZ_13 - 5회
#   2위: TZ_15 - 4회
#   3위: TZ_11 - 4회
#   ...
# ----------------------------------------
# 최다 경고 센서: TZ_13 (5회) → 우선 점검 필요

print("=== 교대조 센서 경고 로그 분석 ===")

morning = ["TZ_11", "TZ_13", "TZ_11", "TZ_15", "TZ_13", "TZ_11", "TZ_11", "TZ_17"]
afternoon = ["TZ_13", "TZ_15", "TZ_13", "TZ_19", "TZ_15", "TZ_21", "TZ_13", "TZ_15"]

# TODO 1. 오전조 / 오후조 각각 고유 센서 종류 수 + 정렬된 목록 출력
#         (set 으로 중복 제거 > sorted 로 정렬)
morning_set = set(morning)
afternoon_set = set(afternoon)
sorted_morning_set = sorted(morning_set)
sorted_afternoon_set = sorted(afternoon_set)
print(f"오전조 고유 센서 4종: {sorted_morning_set}")
print(f"오후조 고유 센서 4종: {sorted_afternoon_set}")

# TODO 2. 교집합 (두 조 모두에서 경고 난 센서) 정렬해서 출력  ( & )
print("----------------------------------------")
inter_set = morning_set.intersection(afternoon_set)
sorted_inter_set = sorted(inter_set)
print(f"양 교대조 공통 경고 센서: {sorted_inter_set}")
# TODO 3. 차집합 (오전 전용 / 오후 전용) 각각 정렬해서 출력  ( - )
#         방향에 따라 결과 다른 것 유의
only_morning = sorted(morning_set.difference(afternoon_set))
only_afternoon = sorted(afternoon_set.difference(morning_set))

print(f"오전조 전용: {only_morning}")
print(f"오후조 전용: {only_afternoon}")
# TODO 4. 합집합 (전체 경고 센서) 종류 수 + 정렬된 목록 출력  ( | )
union_list = sorted(morning_set.union(afternoon_set))

print(f"전체 경고 센서 6종: {union_list}")
print("----------------------------------------")
# TODO 5. 센서마다 (오전 횟수 + 오후 횟수) 구해서
#         (횟수, 센서명) 튜플 리스트 만들고 횟수 많은 순 정렬
#         "N위: 센서명 - X회" 형태로 출력
#         힌트) morning.count("TZ_13") / sorted(리스트, reverse=True)

total_list = []
total_tuple = ()
for i in range(len(union_list)):
    total_tuple = (
        morning.count(union_list[i]) + afternoon.count(union_list[i]),
        union_list[i],
    )
    total_list.append(total_tuple)
total_list.sort(reverse=True)
print(total_list)
print("경고 발생 횟수 순위:")
for idx, value in enumerate(total_list):
    print(f" {idx+1}위: {value[1]} - {value[0]}회")

print("----------------------------------------")
# TODO 6. 가장 경고 많았던 센서 콕 집어서 "우선 점검 필요" 출력
print(f"최다 경고 센서: {total_list[0][1]} ({total_list[0][0]}회) → 우선 점검 필요")

# 도전) 총 3회 이상인 센서만 "집중 관리 대상" 리스트로 만들어 정렬 출력
manage_list = []
for idx, value in enumerate(total_list):
    if value[0] >= 3:
        manage_list.append(value[1])
manage_list.sort()

print(f"집중 관리 대상: {manage_list}")

# =====================================================================
# 종합 실습 1. 설비 종합 모니터링 리포트
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

sensors = [
    ("컨베이어_01", 78, 2.1),
    ("용접기_02", 92, 5.4),
    ("절단기_03", 85, 3.2),
    ("건조로_04", 101, 6.8),
    ("냉각탑_05", 67, 1.5),
    ("도장부스_06", 88, 4.1),
    ("성형기_07", 90, 2.9),
]
# (설비명, 온도, 진동)

# 판정 기준
#   온도 > 90 또는 진동 > 5.0  > "위험"
#   온도 >= 80 또는 진동 >= 3.0 > "주의"
#   그 외                      > "정상"

# TODO 1. 각 설비 상태 판정해서 번호 붙여 한 줄씩 출력 (for + enumerate + if/elif/else)


# TODO 2. 정상 / 주의 / 위험 각각 몇 대인지 세서 출력 (누적변수)


# TODO 3. 이상 설비(주의 + 위험) 비율 % 출력 (round)


# TODO 4. 전체 평균 온도 출력 (round)


# TODO 5. 온도 가장 높은 설비 이름 + 온도 출력 (반복문으로 직접 찾기)


# TODO 6. "위험" 설비 이름만 모아서 정렬해 리스트로 출력 (.append() + .sort())


# 도전) 위험 1대라도 있으면 "⚠ 즉시 점검 요망", 없으면 "✅ 전 설비 안정"
