# SWEA 5656 벽돌깨기
#import sys
#sys.stdin = open("input.txt", "r")
from collections import deque

# DFS로 완전탐색
def dfs(count, N, grid):
    global ans

    # N개 만큼 구슬을 떨어뜨렸다면 남은 블랙의 개수 카운팅 후 ans와 비교하여 종료
    if count == N:
        block_count = 0
        # grid의 각 행별로 행 길이 - 0의 개수
        for row in grid:
            block_count += W - row.count(0)
        # 최소가 되는 ans 채용
        ans = min(ans, block_count)
        return

    # 각 열 별로 순회하며 구슬을 떨어뜨린 경우와 떨어뜨리지 않은 경우 완탐
    for col in range(W):
        new_grid = [row[:] for row in grid]
        drop_ball(new_grid, col)
        dfs(count + 1, N, new_grid)


def down_block(grid):
    check_point = 0         # 0이 처음 시작되는 지점의 체크포인트

    for x in range(W):
        for y in range(H-1, -1, -1):
            # 0값이 나오면 체크포인트 생성
            if grid[y][x] == 0:
                check_point = y
                # 0 값이 나온 지점 이후 부터 조사
                for ny in range(y-1, -1, -1):
                    # 체크포인트가 존재하고 0값이 아니면 스왑 후 체크포인트 초기화
                    if grid[ny][x] != 0 and check_point:
                        grid[y][x], grid[ny][x] = grid[ny][x], grid[y][x]
                        check_point = 0

    #print("블록 가라앉기 종료")

def explosion(grid, dis, sx, sy):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    # 시작지점 Queue에 삽입 및 시작지점 0으로 초기화
    q = deque([(sx, sy, dis)])
    grid[sy][sx] = 0

    while q:
        x, y, dis = q.popleft()

        # 현재 좌표에서 4방향에 대하여
        for d in range(4):
            # 블럭의 숫자-1 만큼 폭발
            for k in range(1, dis):
                nx = x + dx[d] * k
                ny = y + dy[d] * k

                # 다음 좌표가 격자 안이고
                if 0 <= nx < W and 0 <= ny < H:
                    # 다음 좌표가 1이면 0으로 만들고 패스
                    if grid[ny][nx] == 1:
                        grid[ny][nx] = 0
                        continue
                    # 다음 좌표가 0이면 패스
                    elif grid[ny][nx] == 0:
                        continue
                    # 다음 좌표가 1보다 크다면 Queue에 삽입하고 다음 위치 0으로 초기화
                    else:
                        q.append((nx, ny, grid[ny][nx]))
                        grid[ny][nx] = 0
    #print("폭발 종료")

# 정해진 열에서 구슬을 떨어뜨리는 함수
def drop_ball(grid, col):
    for row in range(H):
        # 빈칸이 아닌 블럭이 있다면 폭발 및 중력적용 함수 실행
        if grid[row][col] != 0:
            explosion(grid, grid[row][col], col, row)
            down_block(grid)
            # print(grid)
            break

T = int(input())

'''
Todo list
1. 구슬 N개를 떨어뜨리는 위치
2. 구슬이 블럭에 닿으면 블럭의 숫자에 따라 터지는 매커니즘
3. 블럭의 폭발에 닿으면 연쇄적으로 폭발하는 매커니즘
4. 블럭이 전부 폭발한 후 남은 블럭들이 아래로 떨어지는 매커니즘

* 구슬을 어느위치에 떨어지는 지를 어떻게 정하지?
'''
for test_case in range(1, T+1):
    N, W, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]
    ans = W*H

    dfs(0, N, grid)

    print(f"#{test_case} {ans}")