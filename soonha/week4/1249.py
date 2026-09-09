from collections import deque

T = int(input()) # 테스트케이스 T
for test_case in range(1, T + 1):
    N = int(input()) # 지도의 크기 N
    arr = [list(map(int, input().strip())) for _ in range(N)] # 지도 정보

    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    INF = float('inf')
    dist = [[INF] * N for _ in range(N)] # 각 칸까지의 최소 복구 시간
    dist[0][0] = arr[0][0] # 출발지는 (0, 0)좌표이며, 해당 복구시간은 arr[0][0] 값

    def bfs(x, y):
        q = deque() # 큐 생성
        q.append((x, y)) # 시작 좌표 삽입
        while q:
            x, y = q.popleft() # 큐의 맨 앞에서 꺼냄
            for i in range(4): # 격자의 상, 하, 좌, 우 탐색
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N: # 지도 범위 안에 있을 때
                    new_cost = dist[x][y] + arr[nx][ny]
                    if new_cost < dist[nx][ny]: # 기존 기록보다 적은 비용이 가능하면
                        dist[nx][ny] = new_cost # 값 갱신
                        q.append((nx, ny)) # 갱신된 지점을 큐에 넣어 재탐색

    bfs(0, 0) # 시작 지점부터 BFS 실행
    result = dist[N - 1][N - 1]
    print(f'#{test_case} {result}')