from itertools import combinations
from collections import deque

from itertools import combinations
from collections import deque


def bfs(select_hospital, copied_grid):

    global ans

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    max_cost = 0

    q = deque()

    visited = [[False] * N for _ in range(N)]

    for x, y in select_hospital:
        # 선택된 병원에서 시작
        q.append((x, y, 0))
        visited[y][x] = True

    while q:

        x, y, cost = q.popleft()

        for k in range(4):

            nx = x + dx[k]
            ny = y + dy[k]

            # 범위를 벗어난 경우
            if not (0 <= nx < N and 0 <= ny < N):
                continue

            # 이미 방문한 경우
            if visited[ny][nx]:
                continue

            # 벽인 경우
            if copied_grid[ny][nx] == 1:
                continue

            next_cost = cost + 1

            visited[ny][nx] = True

            # 바이러스인 경우
            if copied_grid[ny][nx] == 0:
                max_cost = max(max_cost, next_cost)

                # 바이러스가 제거된 시간을 기록
                copied_grid[ny][nx] = next_cost

            # 병원(2)도 통과할 수 있음
            q.append((nx, ny, next_cost))

    # 아직 바이러스가 남아있다면
    for row in copied_grid:
        if 0 in row:
            return

    # 모든 바이러스가 제거된 경우
    ans = min(ans, max_cost)
        

# 0 : 바이러스 | 1 : 벽 | 2 : 병원
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
hospitals = []
ans = 1000000

# 병원의 좌표만 모아놓은 리스트
for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            hospitals.append((j, i))

# 병원들의 좌표가 모인 리스트에서 조합으로 M개를 뽑아 새로 리스트를 생성
select_hospitals = list(combinations(hospitals, M))

# 원본 Grid를 복사한 Grid를 조합으로 생선된 리스트와 함께 파라미터로 넘겨줌
for select_hospital in select_hospitals:
    copied_grid = [row[:] for row in grid]
    bfs(select_hospital, copied_grid)

if ans == 1000000:
    ans = -1

print(ans)
