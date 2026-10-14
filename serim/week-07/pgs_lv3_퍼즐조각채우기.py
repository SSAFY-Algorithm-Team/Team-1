# 규칙
# 조각은 한번에 하나씩 채우기
# 조각 회전 가능
# 조각 뒤집기는 불가능
# 게임보드에 새로 채워넣은 퍼즐조각과 인접한 칸 비어있으면 안됨

# 일단 인접한 것들을 이어서 각각의 퍼즐을 알아내야 함

# 그리고 게임 보드에서 흰칸들을 조사해서 퍼즐과 일치하는 공간 있으면 채워넣으면 됨

def in_range(x, y, N):
    return 0 <= x < N and 0 <= y < N


# 상 우 하 좌

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution(game_board, table):

    N = len(game_board)


    visited = [[False]*N for _ in range(N)]

    # 테이블 먼저 조사
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                visited[i][j] == True
                # 4방향 다 순회하기
                





    # 그 후에 게임보드 조사하면서 맞는 칸 채우기

    answer = -1
    return answer