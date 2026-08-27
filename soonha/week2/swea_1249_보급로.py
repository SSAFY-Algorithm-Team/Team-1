from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    dx = [0, 0, -1, 1]  # 상 하 좌 우
    dy = [1, -1, 0, 0]

    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]  # 각 칸까지의 최소 복구 시간
    dist[0][0] = arr[0][0]  # 시작 지점의 복구 시간

    def bfs(start_x, start_y):
        queue = deque()
        queue.append((start_x, start_y))
        while queue:
            x, y = queue.popleft()  # 큐의 맨 앞에서 꺼냄
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N: # 격자 범위 안에 있는 경우에만 계산
                    new_cost = dist[x][y] + arr[nx][ny]
                    if new_cost < dist[nx][ny]:  # 더 짧은 경로를 찾은 경우
                        dist[nx][ny] = new_cost   # 값 갱신
                        queue.append((nx, ny))     # 갱신된 지점을 큐에 추가

    bfs(0, 0)
    result = dist[N - 1][N - 1]
    print(f'#{test_case} {result}')
# DFS 버전
#import sys
#sys.setrecursionlimit(1000000)
#
#T = int(input())
#for test_case in range(1, T + 1):
#    N = int(input())
#    arr = [list(map(int, input())) for _ in range(N)]
#
#    start = (0, 0) # 시작 지점
#    end = (N - 1, N - 1) # 끝 지점
#
#    dp = [[-1] * N for _ in range(N)] # DP(최소 경로 기록을 저장) 
#
#    dx = [0, 0, -1, 1] # 상 하 좌 우
#    dy = [1, -1, 0, 0]
#
#    INF = float('inf')
#    dist = [[INF] * N for _ in range(N)] # 각 칸까지의 최소 복구 시간
#    dist[0][0] = arr[0][0] # 시작 지점의 복구 시간
#
#    def dfs(x, y, cost):
#        for i in range(4):
#            nx, ny = x + dx[i], y + dy[i]
#            if(0 <= nx < N and 0 <= ny < N): # 격자 범위 안에 있는 경우에만 계산
#                new_cost = cost + arr[nx][ny] # 새로운 값 계산
#                if(new_cost < dist[nx][ny]): # 더 짧은 경로를 찾은 경우
#                    dist[nx][ny] = new_cost # 값 갱신
#                    dfs(nx, ny, new_cost) # 갱신된 값으로 탐색
#
#    dfs(0, 0, dist[0][0]) # 시작 지점부터 출발
#    result = dist[N - 1][N - 1] # 도착 지점의 최소 경로 값
#    print(f'#{test_case} {result}') # 출력