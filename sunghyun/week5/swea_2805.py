T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    M = N // 2
    arr = [list(map(int, input())) for _ in range(N)]

    def middle():
        cnt = 0
        for col in range(N):
            cnt += arr[M][col]
        return cnt

    def up():
        cnt = 0
        for d in range(1, M + 1):
            r = M - d
            for col in range(d, N - d):
                cnt += arr[r][col]
        return cnt

    def down():
        cnt = 0
        for d in range(1, M + 1):
            r = M + d
            for col in range(d, N - d):
                cnt += arr[r][col]
        return cnt

    print(f"#{tc} {middle() + up() + down()}")


# abs 사용
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     M = N // 2
#     arr = [list(map(int, input())) for _ in range(N)]
#
#     total = 0
#     for r in range(N):
#         d = abs(r - M)
#         for c in range(d, N - d):
#             total += arr[r][c]
#
#     print(f'#{tc} {total}')
