# swea 5188 최소합

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    grid = [list(map(int, input().split())) for _ in range(N)]
    new_grid = [[float('inf')] * N for _ in range(N)]
    dy = [0, 1]
    dx = [1, 0]

    for i in range(N):
        for j in range(N):
            if i==0 and j==0:
                new_grid[i][j] = grid[i][j]

            for d in range(2):
                nx = j + dx[d]
                ny = i + dy[d]

                if 0 <= nx < N and 0 <= ny < N:
                    temp = new_grid[i][j] + grid[ny][nx]
                    new_grid[ny][nx] = min(new_grid[ny][nx], temp)

    print(f"#{test_case} {new_grid[N-1][N-1]}")