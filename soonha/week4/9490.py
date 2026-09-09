T = int(input()) # 테스트 케이스 T
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    grid = []
    for i in range(N):
        arr = list(map(int, input().split()))
        grid.append(arr)

    max_cnt = -1
    row_grid = [] # 가로 누적합
    # 가로 누적합 계산
    for i in range(N):
        cnt = 0
        arr = []
        for j in range(M):
            cnt += grid[i][j]
            arr.append(cnt)
        row_grid.append(arr)

    col_grid = [] # 세로 누적합
    # 세로 누적합 계산
    for j in range(M):
        cnt = 0
        arr = []
        for i in range(N):
            cnt += grid[i][j]
            arr.append(cnt)
        col_grid.append(arr)

    # 누적합 배열에서 구간 [a, b]의 합을 구하는 함수
    def range_sum(arr, a, b):
        if a <= 0:
            return arr[b]
        return arr[b] - arr[a - 1]

    for row in range(N):
        for col in range(M):
            v = grid[row][col]  # 이 풍선의 꽃가루 개수

            # 가로 방향: 오른쪽 v칸 + 왼쪽 v칸 (중심 중복 제거)
            right = range_sum(row_grid[row], col, min(col + v, M - 1))
            left = range_sum(row_grid[row], max(col - v, 0), col)
            row_total = right + left - v  # 중심(v) 두 번 세었으므로 한 번 빼기

            # 세로 방향: 아래쪽 v칸 + 위쪽 v칸 (중심 중복 제거)
            down = range_sum(col_grid[col], row, min(row + v, N - 1))
            up = range_sum(col_grid[col], max(row - v, 0), row)
            col_total = down + up - v

            # 가로 방향 결과와 세로 방향 결과 모두에 중심이 포함되어 있으므로 한 번 더 빼기
            total = row_total + col_total - v

            if total > max_cnt:
                max_cnt = total

    print(f'#{test_case} {max_cnt}')