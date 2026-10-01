def solution(board, h, w):
    answer = 0
    n = len(board)
    count = 0
    cur_color = board[h][w]
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]

    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]

        if 0 <= nh < n and 0 <= nw < n:
            if cur_color == board[nh][nw]:
                count += 1

    answer = count
    return answer