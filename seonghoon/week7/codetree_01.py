# https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/baggage-conveyor-belt/description
from collections import deque

# 현재 컨베이어에 올라가 있는 수하물 정보를 나타내는 클래스
class luggage:
    # ID, 수하물의 무게, 막힌 횟수, 파손 여부
    def __init__(self, id, weight, stuckcnt = 0, isbroke = False):
        self.id = id
        self.weight = weight
        self.stuckcnt = stuckcnt
        self.isbroke = isbroke

# 컨베이어에 추가되기를 기다리는 수하물 정보
class wait_luggage:
    # ID, 추가될 시점 턴, 초기좌표, 수하물의 무게
    def __init__(self, id, turn, axis, weight):
        self.id = id
        self.turn = turn
        self.axis = axis
        self.weight = weight

# X, 하, 좌, 상, 우
dy = [0, 1, 0, -1, 0]
dx = [0, 0, -1, 0, 1]

# 컨베이어 벨트 정보를 담은 2차원 리스트.
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
lug_end = []            # 컨베이어 벨트의 도착 지점
for y in range(N):
    for x in range(N):
        if grid[y][x] == 9:
            lug_end.append((y, x))

# 수하물 대기 정보 추가
luggage_list = []
B = int(input())
for id in range(B):
    turn, y, x, weight = map(int, input().split())
    luggage_list.append(wait_luggage(id, turn, (y-1, x-1), weight))

# 대기 수하물을 턴 수 기준 오름차순 정렬
luggage_list.sort(key=lambda x: x.turn)

arrival_time = [0] * B                          # 수하물 id별 도착 시간을 담을 리스트
lug_grid = [[None] * N for _ in range(N)]       # 컨베이어 벨트 위 수하물 정보를 담는 그리드

# 시뮬레이션 시작
for cturn in range(1, 201):
    # 1, 2단계: 수하물 이동 후 적재 & 파손 처리
    # 전략 : 도착지점부터 역순 BFS를 통해 수하물 이동 시뮬레이션
    q = deque()
    for axis in lug_end:
        q.append(axis)
    while q:
        cy, cx = q.popleft()
        # if cturn==1:
        #     print(cy, cx)

        # 현위치의 상하좌우의 컨베이어 벨트가 현재 좌표를 바라보고 있고, 그 자리에 수하물이 있다면
        # 수하물의 좌표와 수하물 정보 포인터를 가져와서 저장함.
        cand_lug = []
        for d in range(1, 5):
            ny, nx = cy + dy[d], cx + dx[d]
            if ny<0 or ny>=N or nx<0 or nx>=N:          # 범위 밖
                continue
            if grid[ny][nx] in (0, 9):          # 컨베이어 벨트가 아닌 경우
                continue
            if (ny + dy[grid[ny][nx]], nx + dx[grid[ny][nx]]) != (cy, cx):        # 벨트가 현재 좌표로 오는 방향이 아님
                continue
            q.append((ny, nx))              # 수하물이 있든 없든 일단 컨베이어가 연결되어 있으므로 큐에 추가
            if lug_grid[ny][nx] is None:                # 수하물 없음
                continue
            cand_lug.append((ny, nx, lug_grid[ny][nx]))        # 후보 수하물 목록에 추가

        # 후보 수하물이 없다면 다음 좌표로 넘어감
        if not cand_lug:
            continue

        # 수하물을 weight 기준 내림차순, id 기준 오름차순 정렬
        cand_lug.sort(key=lambda x: (-x[2].weight, x[2].id))
        # 수하물을 현재 좌표로 옮기고, 현재 좌표에 오지 못한 수하물은 stuckcnt 증가
        for ny, nx, lug in cand_lug:
            if lug_grid[cy][cx] is None:
                lug_grid[cy][cx] = lug
                lug_grid[ny][nx] = None
                lug.stuckcnt = 0
            else:
                lug.stuckcnt += 1
                # stuckcnt가 3 이상이면 파손 처리
                if lug.stuckcnt >= 3:
                    lug.isbroke = True

        # 도착지점에 수하물이 있다면 도착 시간을 기록하고 수하물 소멸
        if (cy, cx) in lug_end and lug_grid[cy][cx] is not None:
            lug = lug_grid[cy][cx]
            arrival_time[lug.id] = cturn * (-1 if lug.isbroke else 1)
            lug_grid[cy][cx] = None

    # 3단계: 컨베이어 벨트에 추가
    for lug in luggage_list:
        if lug.turn == -1:
            continue
        # 컨베이어에 추가 가능한 턴이며, 위치가 비어있을 때 추가 가능
        if lug.turn <= cturn:
            y, x = lug.axis
            if lug_grid[y][x] is None:
                conv_lug = luggage(lug.id, lug.weight)
                lug_grid[y][x] = conv_lug
                lug.turn = -1
        else:
            break

# 시뮬레이션 종료 후 결과 출력
print(*arrival_time)