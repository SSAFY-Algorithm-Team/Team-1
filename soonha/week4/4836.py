T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    grid = [[0] * 10 for _ in range(10)]
    '''
    color: 1은 빨강, 2는 파랑 -> 보라색(빨강 + 파랑) 영역을 찾아야 하므로 보라색 영역을 3이라고 설정한다
    '''
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split()) # 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color
        for j in range(r1, r2 + 1): # r1 행부터 r2 행까지
            for k in range(c1, c2 + 1): # c1 열부터 c2 열까지
                if(grid[j][k] == 0): # 아직 색칠이 안되어 있으면
                    grid[j][k] = color # 해당 색으로 색칠
                elif(grid[j][k] == 1): # 빨간색이 칠해져 있는 경우
                    if(color == 2): # 칠해야 하는 color가 파란색일 때
                        grid[j][k] = 3 # 보라색으로 설정
                elif(grid[j][k] == 2): # 파란색이 칠해져 있는 경우
                    if(color == 1): # 칠해야 하는 color가 빨간색일 때
                        grid[j][k] = 3 # 보라색으로 설정

    # 탐색
    result = 0
    for row in range(10):
        for col in range(10):
            if(grid[row][col] == 3): # 보라색이면
                result += 1 # 값 추가

    print(f'#{test_case} {result}')