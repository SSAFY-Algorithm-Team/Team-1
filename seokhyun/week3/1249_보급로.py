# swea 1249 보급로
from collections import deque
import sys
sys.stdin = open("input.txt", "r")

def bfs(x, y):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    q = deque([(0,0)])

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[ny][nx] > visited[y][x] + grid[ny][nx]:
                    visited[ny][nx] = visited[y][x] + grid[ny][nx]
                    q.append((nx, ny))

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[float('inf')] * N for _ in range(N)]
    visited[0][0] = 0

    bfs(0, 0)

    print(f"#{test_case} {visited[N-1][N-1]}")