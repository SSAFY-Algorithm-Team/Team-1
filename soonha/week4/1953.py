from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    # 세로 크기 N, 가로 크기 M, 시작점 세로 위치 R, 가로 위치 C, 탈출 후 소요 시간 L
    N, M, R, C, L = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)] # 지하 터널 격자
    visited = [[False] * M for _ in range(N)] # 방문 가능 여부를 다루는 격자

    # 각 터널 타입의 연결 방향 [상= (-1,0), 하= (1,0), 좌= (0,-1), 우 =(0,1)]
    DIRS = {
        1: [(-1, 0), (1, 0), (0, -1), (0, 1)],  # 상 하 좌 우
        2: [(-1, 0), (1, 0)],  # 상 하
        3: [(0, -1), (0, 1)],  # 좌 우
        4: [(-1, 0), (0, 1)],  # 상 우
        5: [(1, 0), (0, 1)],  # 하 우
        6: [(1, 0), (0, -1)],  # 하 좌
        7: [(-1, 0), (0, -1)],  # 상 좌
    }
    OPPOSITE = {(-1, 0): (1, 0),
                (1, 0): (-1, 0),
                (0, -1): (0, 1),
                (0, 1): (0, -1)}

    def bfs(R, C, time): # x좌표 R, y좌표 C, 소요 시간 time
        q = deque() # 큐 생성
        q.append((R, C, time)) # 큐에 삽입
        visited[R][C] = True # 시작점은 True 설정
        while q:
            x, y, cnt = q.popleft()
            if cnt >= L: # 더 이상 이동할 시간이 없으면
                continue
            tunnel_type = grid[x][y] # 현재 좌표의 터널 타입 확인
            if tunnel_type == 0: # 터널이 연결되어 있지 않으면
                continue

            for dx, dy in DIRS[tunnel_type]:
                nx, ny = x + dx, y + dy
                if(0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False): # 격자 범위 안이고 아직 방문을 안했다면
                    next_type = grid[nx][ny] # 방문할 곳의 터널 상태 확인
                    if next_type == 0: # 방문할 곳이 터널이 없다면 패스
                        continue
                    if OPPOSITE[(dx, dy)] in DIRS[next_type]: # 이웃도 반대 방향에 연결되어 있어야 함
                        visited[nx][ny] = True
                        q.append((nx, ny, cnt + 1))

    bfs(R, C, 1)
    result = sum(visited[i][j] for i in range(N) for j in range(M))

    print(f'#{test_case} {result}')