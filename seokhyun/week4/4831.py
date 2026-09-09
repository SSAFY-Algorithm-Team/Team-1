# SWEA 4831

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # K : 한번에 최대 이동 칸 수, N : 종점, M : 설치된 충전기 개수
    K, N, M = map(int, input().split())
    charger = set(map(int, input().split()))
    res = 0
    cur_pos = 0
    flag = False        # 충전소 유무를 나타내는 상태 변수

    # 현재 위치에서 한 Step 안에 종점이 없는 동안 loop
    while cur_pos + K < N:
        flag = False            # 매 Step 마다 충전소 발견 상태 초기화

        # 시작지점에서 최대 step으로 점프 후 뒤로 이동하며 충전소 찾기
        for i in range(cur_pos + K, cur_pos, -1):
            if i in charger:    # 현재 위치에 충전소가 있는가?
                res += 1
                cur_pos = i     # 충전소를 발견하면 현재 위치 갱신
                flag = True     # 충전소 발견했다는 상태 갱신
                break

        if flag == False:       # 한 Step 범위에 충전소 없음 => loop 종료
            res = 0
            break

    print(f"#{test_case} {res}")