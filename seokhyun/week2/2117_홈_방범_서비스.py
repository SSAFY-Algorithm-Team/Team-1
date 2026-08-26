# SWEA 2117 홈 방범 서비스
from collections import deque

def bfs(x, y):
    global res
    visited = [[False] * N for _ in range(N)]
    k = 1
    count = 0

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    q = deque([(x, y)])
    visited[y][x] = True


    # 시작 지점에 집이 있는가?
    if grid[y][x] == 1:
        count += 1

    while q:
        cost = k*k + (k-1)*(k-1)
        revenue = count * M

        # 요구 비용보다 얻는 수익이 많은가?
        if cost <= revenue:
            res = max(res, count)

        # q가 다 빌때까지 loop 그래야 K가 늘어날 수 있음
        for _ in range(len(q)):
            cx, cy = q.popleft()

            # center를 중심으로 상하좌우 전부 조회
            for d in range(4):
                nx = cx + dx[d]
                ny = cy + dy[d]

                # 다음 좌표가 격자 내부이면서 방문하지 않은 경우
                if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                    visited[ny][nx] = True

                    if grid[ny][nx] == 1:
                        count += 1

                    q.append((nx, ny))
        k += 1

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    res = 0

    for y in range(N):
        for x in range(N):
            bfs(x, y)

    print(f"#{test_case} {res}")
