# swea 5105 미로의 거리
from collections import deque

def bfs(x, y, dist):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    q = deque([(x, y, dist)])
    visited = [[False] * N for _ in range(N)]
    visited[y][x] = True

    while q:
        cx, cy, cd = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
        
            if 0 <= nx < N and 0 <= ny < N:
                if maze[ny][nx] == 3:
                    return cd
                elif maze[ny][nx] != 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((nx,ny,cd+1))
    return 0
    
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    dist = 0
    start_pos = (0, 0)

    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                start_pos = (x, y)

    res = bfs(*start_pos, dist)

    print(f"#{test_case} {res}")