from collections import deque

for test_case in range(10):
    T = int(input())
    grid = [list(map(int, input().strip())) for _ in range(16)] # 16 * 16 격자 입력받기
    '''
    0: 길, 1: 벽, 2: 출발점, 3: 도착점
    '''
    visited = [[False] * 16 for _ in range(16)] # 16 * 16 격자의 방문 여부를 저장하는 격자

    for i in range(16):
        for j in range(16):
            if(grid[i][j] == 2): # 해당 좌표가 출발점이면
                start = (i, j) # 시작 좌표 설정
            if(grid[i][j] == 3): # 해당 좌표가 도착점이면
                end = (i, j) # 도착 좌표 설정
    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    def bfs(location):
        q = deque() # 큐 생성
        q.append(location) # 시작 좌표 삽입
        while q:
            x, y = q.popleft() # 좌표 확인
            visited[x][y] = True  # 해당 좌표 방문
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if(0 <= nx < 16 and 0 <= ny < 16): # 격자 범위 안이면
                    if((grid[nx][ny] == 0 or grid[nx][ny] == 3) and visited[nx][ny] == False): # 갈 수 있는 길이고 아직 안 갔다면
                        q.append((nx, ny))

    bfs(start) # 좌표 탐색 실행
    if visited[end[0]][end[1]] == True:
        result = 1
    else:
        result = 0

    print(f'#{T} {result}')