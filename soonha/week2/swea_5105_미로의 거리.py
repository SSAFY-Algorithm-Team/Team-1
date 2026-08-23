from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maze = [input().strip() for _ in range(N)] # 미로 정보를 N개의 문자열 줄로 저장

    start = None # 출발 위치(2)
    goal = None # 도착 위치(3)
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2': # 출발 위치에 해당하면
                start = (i, j) # 해당 좌표 저장
            elif maze[i][j] == '3': # 도착 위치에 해당하면
                goal = (i, j) # 해당 좌표 저장

    def bfs(start, goal):

        visited = [[False] * N for _ in range(N)] # 방문 여부를 저장
        dist = [[0] * N for _ in range(N)]  # 시작점부터 몇 번 이동했는지 저장

        q = deque()
        q.append(start)
        visited[start[0]][start[1]] = True

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while q:
            x, y = q.popleft()
            if (x, y) == goal:
                return dist[x][y] - 1

            for d in range(4): # 상하좌우 반영
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    if not visited[nx][ny] and maze[nx][ny] != '1':
                        visited[nx][ny] = True
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))

        return 0  # 도달 불가능의 경우 리턴

    result = bfs(start, goal) # BFS 실행 결과 저장
    print(f'#{test_case} {result}') # 출력