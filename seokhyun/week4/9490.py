# SWEA 9490 풍선팡
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    res = 0

    for i in range(N):
        for j in range(M):
            temp = grid[i][j]
            p = temp

            # 현재 위치의 풍선 거리만큼 터져요
            for d in range(4):
                for k in range(1, p+1):
                    nx = j + dx[d] * k
                    ny = i + dy[d] * k

                    if 0 <= nx < M and 0 <= ny < N:
                        temp += grid[ny][nx]

            if res <= temp:
                res = temp

    print(f"#{test_case} {res}")