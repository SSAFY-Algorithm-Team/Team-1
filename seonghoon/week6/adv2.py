from itertools import combinations
from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

hospital = []
viruses = 0

# 병원이 있는 곳 기록 후, 빈칸으로 남김. 그 이후 빈칸의 개수를 세어 바이러스 수를 계산함.
for y in range(N):
    for x in range(N):
        if grid[y][x] == 2:
            hospital.append((y, x))
        elif grid[y][x] == 0:
            viruses += 1

def bfs(active_hosp, grid, viruses):
    q = deque()
    visited = [[False] * N for _ in range(N)]
    for y, x in active_hosp:
        q.append((y, x, 0))
        visited[y][x] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        y, x, time = q.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and grid[ny][nx] != 1:
                visited[ny][nx] = True
                q.append((ny, nx, time + 1))
                if grid[ny][nx] == 0:
                    viruses -= 1
                if viruses == 0:
                    return time + 1
    return float('inf')

min_time = float('inf')
for active_hosp in combinations(hospital, M):
    if viruses == 0:
        min_time = 0
        break
    # 활성화된 병원 기준 백신 퍼뜨리기 bfs 수행
    result = bfs(active_hosp, [row[:] for row in grid], viruses)
    min_time = min(min_time, result)

print(min_time if min_time != float('inf') else -1)