from collections import deque

# 빈칸을 열 번호가 작은 순서, 같은 열에서는 아래쪽 행부터 채운다.
def fill_relics(relics, sub_relics):
    for i in range(5):
        for j in range(4, -1, -1):
            # 빈칸(0)을 발견하면 예비 유물로 채운다.
            if relics[j][i] == 0:
                # 예비 유물이 없으면 현재 열의 빈칸 채우기를 중단한다.
                if not sub_relics:
                    break

                # 예비 유물을 입력된 순서대로 꺼내 빈칸에 넣는다.
                relics[j][i] = sub_relics.pop(0)

    return relics


# 획득 대상 유물을 제거하고 빈칸을 예비 유물로 채운다.
def acquire(relics, res_relics, sub_relics):
    global ans

    # 획득 대상 좌표의 유물을 제거하고 획득 개수를 누적한다.
    for x, y in res_relics:
        relics[y][x] = 0
        ans += 1

    # 제거한 유물의 빈자리를 예비 유물로 채운다.
    relics = fill_relics(relics, sub_relics)

    return relics


# 상하좌우로 연결된 같은 숫자의 그룹을 탐색하고,
# 크기가 3 이상인 그룹의 총점과 해당 좌표들을 반환한다.
def search(relics):
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    cur_piece = []
    res_piece = []

    visited = [[False] * 5 for _ in range(5)]
    res = 0

    for i in range(5):
        for j in range(5):
            ## 이미 방문했거나 빈칸인 곳은 탐색하지 않는다.
            if visited[i][j] or relics[i][j] == 0:
                continue

            # 현재 탐색 그룹의 크기와 기준 숫자를 초기화한다.
            cur_cost = 1
            cur_num = relics[i][j]
            visited[i][j] = True

            # BFS를 사용해 같은 숫자로 연결된 칸을 탐색.
            # 좌표는 (열, 행) 순서로 큐에 저장한다.
            q = deque([(j, i)])
            cur_piece.append((j, i))

            while q:
                x, y = q.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    # 다음 좌표가 격자 범위 안에 있는가?.
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        # 아직 방문하지 않았고 기준 숫자와 같은가?.
                        if not visited[ny][nx]:
                            if relics[ny][nx] == cur_num:
                                visited[ny][nx] = True
                                cur_cost += 1
                                cur_piece.append((nx, ny))
                                q.append((nx, ny))

            # 인접한 유물의 크기가 3 이상이면 좌표와 점수를 누적한다.
            if cur_cost >= 3:
                res_piece.extend(cur_piece)
                res += cur_cost

            # 다음 그룹을 탐색하기 위해 현재 그룹의 좌표 목록을 비운다.
            cur_piece.clear()

    # 획득 가능한 그룹이 하나도 없으면 -1과 빈 좌표 목록을 반환한다.
    if res == 0:
        return -1, []

    return res, res_piece


# 모든 3x3 영역을 세 가지 각도로 회전해 최적의 결과를 찾는다.
def explore(relics):
    max_grid = []
    max_piece = []
    cur_cost = 0
    max_x = 0
    max_y = 0
    max_spin = 0
    best = None

    # 5x5 격자에서 3x3 영역의 시작 좌표 9개를 모두 확인한다.
    for y in range(3):
        for x in range(3):
            new_grid = [row[:] for row in relics]

            # 선택한 영역을 90도, 180도, 270도 순서로 회전한다.
            for spin in range(3):
                rotated = [row[:] for row in new_grid]

                # 선택한 3x3 영역만 시계 방향으로 90도 회전한다.
                for i in range(3):
                    for j in range(3):
                        # 회전 영역의 시작 좌표가 (x, y)이므로
                        # 원본과 대상 좌표에 시작 좌표를 반영.
                        rotated[y + j][x + 2 - i] = new_grid[y + i][x + j]

                # 이번 회전 결과를 다음 회전의 입력으로 사용한다.
                new_grid = rotated

                # 회전 결과에서 획득 가능한 점수와 유물 좌표를 계산한다.
                cur_cost, cur_piece = search(new_grid)

                # 점수는 클수록, 회전 횟수와 중심 열·행 번호는 작을수록 우선한다.
                # 음수를 사용하면 튜플의 큰 값 우선 비교로 이 우선순위를 구현할 수 있다.
                candidate = (cur_cost, -spin, -(x + 1), -(y + 1))

                # 첫 후보이거나 기존 최선의 후보보다 우선순위가 높으면 갱신한다.
                if best is None or candidate > best:
                    best = candidate
                    max_grid = [row[:] for row in new_grid]
                    max_piece = cur_piece[:]
                    max_spin = spin
                    max_x = x + 1
                    max_y = y + 1

    # 최적의 회전 격자, 획득 대상 좌표, 최초 획득 점수를 반환한다.
    return max_grid, max_piece, best[0]


'''
작업의 순서를 잘 정해야 한다.
1. 유물 탐사 (회전)
-> 회전 중심이 1,1 ~ 3,3 까지 총 9칸, 3회전 >> 총 27번의 회전 격자가 만들어짐
-> 모든 상황에서 회전해야 함

2. 유물 최대 코스트 비교
-> 어떠한 위치에서 몇 도의 회전을 하였을 때 1차 획득의 가치가 가장 큰 가?
-> (1) 회전 각도가 가장 작고, (2) 중심 좌표 열이 가장 작은 구간, (3) 중심 좌표 행이 가장 작은 구간

3. 유물 획득
-> 3개 이상의 유물을 획득한 후 빈 공간에 유적 벽면의 유물 조각이 삽입된다.
-> 유물 조각은 빈 칸의 (1)열 번호가 작은 순서, (2) 행 번호가 큰 순서 로 생겨난다.
'''

K, M = map(int, input().split())
relics = [list(map(int, input().split())) for _ in range(5)]
sub_relics = list(map(int, input().split()))
res_piece = []
ans = 0

## 최대 K턴 동안 탐사를 진행한다.
for _ in range(K):
    ## 이번 턴에서 최적의 회전 결과와 최초 획득 대상 좌표 및 점수를 구한다.
    relics, res_piece, score = explore(relics)

    ## 최초 획득 점수가 0 이하라면 더 이상 탐사를 진행하지 않는다.
    if score <= 0:
        break

    ## 최초 획득 이후 추가로 획득할 그룹이 있는 동안 연쇄 획득을 진행한다.
    while res_piece:
        # 현재 획득 대상 유물을 제거하고 빈칸을 채운다.
        relics = acquire(relics, res_piece, sub_relics)

        # 보충 이후 새로 획득 가능한 그룹을 탐색한다.
        cur_cost, res_piece = search(relics)

        # 추가 획득 대상이 없으면 이번 턴의 연쇄 획득을 종료.
        if cur_cost == -1:
            break

    # 이번 턴에 획득한 유물 수를 출력하고 다음 턴을 위해 초기화한다.
    print(ans, end=' ')
    ans = 0