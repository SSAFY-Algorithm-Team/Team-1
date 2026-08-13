T = int(input())  # 테스트케이스 개수

for tc in range(1, T + 1):
    data = list(input().split())

    N = int(data[0])       # 눌러야 하는 버튼 개수
    tokens = data[1:]      # 로봇/위치 쌍이 나열된 부분: ['B','2','O','1','O','2','B','4', ...]

    last_time = {'O': 0, 'B': 0}   # 로봇별 마지막 누름 시각
    last_pos = {'O': 1, 'B': 1}    # 로봇별 마지막 누름 당시 위치

    global_time = 0 # "가장 최근에 눌린 버튼의 시각"

    for k in range(N):
        robot = tokens[2 * k]        # 이번에 눌러야 하는 로봇 ('O' 또는 'B')
        x = int(tokens[2 * k + 1])   # 눌러야 하는 버튼의 위치(정수)

        dist = abs(x - last_pos[robot])
        robot_time = last_time[robot] + dist + 1 # 해당 로봇이 버튼을 누르는 가장 이른 시각

        time_order = global_time + 1 # 순서 상 가장 이르게 누를 수 있는 시각(로봇이 동시에 버튼을 누르는 것을 방지)

        t = max(robot_time, time_order) # 실제로 만족하는 가장 최소 시각

        last_time[robot] = t # 시간 업데이트
        last_pos[robot] = x # 위치 업데이트
        global_time = t # 시간 업데이트

    print(f'#{tc} {global_time}')