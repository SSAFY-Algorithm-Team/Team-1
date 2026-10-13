from collections import deque


def search(relics):
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    visited = [[False] * 5 for _ in range(5)]
    res = 0

    for i in range(5):
        for j in range(5):
            # 이미 방문한 곳은 볼 필요 없다.
            if visited[i][j] == True:
                continue

            cur_cost = 1
            cur_num = relics[i][j]
            visited[i][j] = True

            q = deque([(j, i)])

            while q:
                x, y = q.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    # 격자 범위 안에 있어야 하고
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        # 방문한 적이 없어야 하고
                        if not visited[ny][nx]:
                            # 탐색 시작점의 숫자와 같은 곳이어야 한다.
                            if relics[ny][nx] == cur_num:
                                visited[ny][nx] = True
                                cur_cost += 1
                                q.append((nx, ny))

            if cur_cost >= 3:
                # print(cur_cost)
                res += cur_cost

    return res


def rotate(relics):
    # grid_2 = [row[:] for row in relics]
    # grid_3 = [row[:] for row in relics]
    max_grid = []
    max_cost = 0
    cur_cost = 0
    center_r = 0
    center_c = 0
    spin = 0

    for y in range(0, 3):
        for x in range(0, 3):
            grid_1 = [row[:] for row in relics]

            for i in range(y, y + 3):
                for j in range(x, x + 3):
                    grid_1[j][3 - i - 1] = relics[i][j]
                    # grid_2[3-i-1][3-j-1] = relics[i][j]
                    # grid_3[3-j-1][i] = relics[i][j]

            cur_cost = search(grid_1)

            # 현재 코스트가 더 크다면?
            if cur_cost > max_cost:
                max_cost = cur_cost
                center_r = y + 1
                center_c = x + 1

            # 만약 비용이 같다면?
            elif cur_cost == max_cost:
                # 회전 횟수를 비교한다.
                if max_spin < spin:
                    pass
                # 회전 횟수가 같다면 열과 행을 비교한다.
                elif max_spin == spin:
                    # 열 idx 비교
                    if center_c < x + 1:
                        pass
                    # 열 크기도 같다면 행 크기 비교
                    elif center_c == x + 1:
                        # 행 크기 비교
                        if center_r < y + 1:
                            pass
                        elif center_r == y + 1:


'''
작업의 순서를 잘 정해야 한다.
1. 유물 탐사 (회전)
-> 회전 중심이 1,1 ~ 3,3 까지 총 9칸, 3회전 >> 총 27번의 회전 격자가 만들어짐

2. 유물 최대 코스트 비교
-> 어떠한 위치에서 몇 도의 회전을 하였을 때 1차 획득의 가치가 가장 큰 가?
-> (1) 회전 각도가 가장 작고, (2) 중심 좌표 열이 가장 작은 구간, (3) 중심 좌표 행이 가장 작은 구간

3. 유물 획득
-> 3개 이상의 유물을 획득한 후 빈 공간에 유적 벽면의 유물 조각이 삽입된다.
-> 유물 조각은 빈 칸의 (1)열 번호가 작은 순서, (2) 행 번호가 큰 순서 로 생겨난다.
'''
K, M = map(int, input().split())
relics = [list(map(int, input().split())) for _ in range(5)]
piece_of_relics = list(map(int, input().split()))

rotate(relics)