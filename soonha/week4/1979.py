# swea_1979
T = int(input()) # 테스트 케이스 T
for test_case in range(1, T + 1):
    N, K = map(int, input().split()) # 단어 퍼즐의 가로, 세로 길이 N, 단어의 길이 K
    grid = [] # 단어 퍼즐을 저장할 격자(단어 입력 가능: 1, 입력 불가: 0)
    for _ in range(N): # 단어 퍼즐 격자 입력
        arr = list(map(int, input().split()))
        grid.append(arr)

    result = 0 # 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수

    # 가로로 가능한 경우
    for row in range(N):
        for col in range(N):
            cnt = 0 # 자릿수를 계산하는 변수
            # 이 칸이 가로 자리의 시작점인지 확인
            if(grid[row][col] == 1 and (col == 0 or grid[row][col - 1] == 0)):
                cnt += 1 # 자릿수 추가
                i = 1
                while(True):
                    # 격자 범위 안에 있고 여전히 단어가 들어갈 수 있으면
                    if(0 <= col + i < N and grid[row][col + i] == 1):
                        cnt += 1 # 자릿수 추가
                        i += 1 # 우로 1칸 이동
                    else: # 격자 범위를 벗어나거나 또는 단어가 들어갈 수 없으면
                        break # while문 탈출
                # 값 비교
                if(cnt == K): # 단어가 들어갈 수 있으면
                    result += 1 # 결과에 추가

    # 세로로 가능한 경우
    for col in range(N):
        for row in range(N):
            cnt = 0 # 자릿수를 계산하는 변수
            # 이 칸이 세로 자리의 시작점인지 확인
            if(grid[row][col] == 1 and (row == 0 or grid[row - 1][col] == 0)):
                cnt += 1 # 자릿수 추가
                i = 1
                while(True):
                    # 격자 범위 안에 있고 여전히 단어가 들어갈 수 있으면
                    if(0 <= row + i < N and grid[row + i][col] == 1):
                        cnt += 1 # 자릿수 추가
                        i += 1 # 하로 1칸 이동
                    else: # 격자 범위를 벗어나거나 또는 단어가 들어갈 수 없으면
                        break # while문 탈출
                if(cnt == K): # 단어가 들어갈 수 있으면
                    result += 1 # 결과에 추가

    print(f'#{test_case} {result}') # 출력