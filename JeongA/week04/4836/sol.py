import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=" ")

    # 색칠 영역의 개수
    N = int(input())

    matrix = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        start_row, start_col, fin_row, fin_col, color = map(int, input().split())

        for i in range(start_row, fin_row+1):
            for j in range(start_col, fin_col+1):
                if not matrix[i][j]:
                    matrix[i][j] = color
                elif matrix[i][j] != color:
                    matrix[i][j] = 3

    # 색칠이 끝나고 보라색의 개수 계산
    cnt = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 3:
                cnt += 1

    print(cnt)