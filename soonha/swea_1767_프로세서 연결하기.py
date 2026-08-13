"""
백트래킹(Backtracking): "가능한 모든 경우를 하나씩 시도해보되, 답이 될 수 없다는 게 확실해지는 순간 즉시 포기하고 되돌아가는" 탐색 기법
"""
def solve(N, grid): # N x N 격자에 대해 최대 연결 시 최소 전선 길이 합을 구하는 함수
    def is_border(r, c):
        """
    	가장자리에는 이미 전원이 흐르고 있으므로, 여기 있는 Core는 전선 없이 자동 연결됨
    	"""
        return r == 0 or r == N - 1 or c == 0 or c == N - 1 # (r, c) 셀이 격자의 가장자리(테두리)에 위치하는지 판별

    cores = [(r, c) for r in range(N) for c in range(N) if grid[r][c] == 1] # 격자 전체를 훑어서 Core(1)의 좌표를 모두 수집
    """
    cores = []                          
	for r in range(N):                
    	for c in range(N):            
        	if grid[r][c] == 1: 
            	cores.append((r, c))
    """
    interior = [(r, c) for (r, c) in cores if not is_border(r, c)] # 수집한 Core 중에서 가장자리가 아닌 것들만 따로 분리 (전선을 놓아야 하는 Core)
    base_count = len(cores) - len(interior) # 자동 연결된(가장자리에 있는) Core 갯수
    used = [[False] * N for _ in range(N)] # 전선이 있는 지 여부를 저장하는 격자(True면 그 셀이 이미 다른 Core의 전선이 있음)
    n = len(interior)  # 전선을 놓아야 할 Core의 갯수
    best = [0, 0] # best[0]: 지금까지 찾은 최대 연결된 Core 개수 / best[1]: best[0]개를 연결했을 때의 최소 전선 길이 합
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우 정의
    
	# (r, c)에 있는 Core에서 (dr, dc) 방향으로 직선으로 나아갈 때, 가장자리에 도달할 때까지 거쳐야 하는 격자들의 좌표 리스트를 반환하는 함수
    def get_path(r, c, dr, dc): 
        cells = []  # 지나가게 될 격자들을 담을 리스트
        rr, cc = r + dr, c + dc  # Core 바로 옆 칸부터 시작
        while 0 <= rr < N and 0 <= cc < N: # 격자 범위 안에 있는 동안 계속 진행
            cells.append((rr, cc))  # 현재 칸을 경로에 추가
            if rr == 0 or rr == N - 1 or cc == 0 or cc == N - 1: # 가장자리 칸에 도달했다면, 해당 좌표에서 전원과 연결되므로 경로 완성
                return cells
            rr += dr  # 다음 칸으로 이동 (행)
            cc += dc  # 다음 칸으로 이동 (열)
        return None # while문을 빠져나왔다는 것은 가장자리에 닿기 전에 격자를 벗어났다는 뜻인데, Core가 가장자리가 아닌 위치에서 시작했다면 이론상 발생하지 않음
	
    # 주어진 경로(cells)가 실제로 전선을 놓을 수 있는 경로인지 검사
    def valid(cells):
        for (rr, cc) in cells:
            if grid[rr][cc] == 1 or used[rr][cc]: # 경로 중간에 다른 Core가 있거나, 이미 다른 전선이 지나갔다면
                return False # 이 경로는 사용할 수 없음
        return True  # 격자가 비어 있고 아직 전선이 없다면 유효한 경로

    def backtrack(idx, count, length):
        """
        idx: 지금 몇 번째 내부 Core를 처리하려는 중인지
        count: 지금까지 연결하기로 확정한 내부 Core 개수
        length: 지금까지 사용한 전선 길이의 합
        """
        if count > best[0] or (count == best[0] and length < best[1]): # 개수가 더 많으면 무조건 갱신, 개수가 같다면 길이가 더 짧을 때만 갱신
            # 현재 상태가 지금까지의 최선(best)보다 낫다면 best 값을 갱신
            best[0] = count
            best[1] = length
            
        if idx == n: # 모든 Core에 대한 결정을 마쳤다면 더 진행할 것이 없으므로 종료
            return
        
        remaining = n - idx  # 아직 결정되지 않은 Core 개수
        
        if count + remaining < best[0]:  # 남은 Core를 전부 연결해도 현재 best의 개수를 넘을 수 없다면 탐색 중단
            return
        
        if count + remaining == best[0] and length >= best[1]: # 남은 Core를 전부 연결해도 best와 개수가 같을 뿐이고 이미 사용한 길이가 best의 길이 이상이라면, 더 진행해봐야 개선될 수 없으므로 중단
            return
        
        r, c = interior[idx]  # 지금 처리할 Core의 좌표
        options = []  # 이 Core를 연결할 수 있는 유효한 방향별 경로들을 모아둘 리스트
        for dr, dc in directions:
            path = get_path(r, c, dr, dc)  # 해당 방향으로의 경로 계산
            if path and valid(path):
                options.append(path) # 경로가 존재하고 유효하다면 후보에 추가
                
        for path in options: # 후보로 나온 각 경로에 대해 이 Core를 이 방향으로 연결한다는 선택을 시도
            for (rr, cc) in path:
                used[rr][cc] = True  # 이 경로가 지나가는 모든 칸을 전선이 깔린 것으로 처리
            backtrack(idx + 1, count + 1, length + len(path)) # 다음 Core로 넘어가서 계속 탐색 (연결 개수 +1, 길이는 이 경로 길이만큼 증가)
            for (rr, cc) in path:
                used[rr][cc] = False  # 되돌아왔으니 전선이 안 깔린 상태로 원복(백트래킹)
        backtrack(idx + 1, count, length) # 이 Core를 아예 연결하지 않는 선택지도 시도 (개수/길이 변화 없이 다음 Core로)
        
    backtrack(0, 0, 0)  # 0번째 Core부터, 연결 개수 0, 길이 0으로 탐색 시작
    return best[1]  # 최대 Core개수를 연결했을 때의 최소 전선 길이 합을 반환

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    data = []
    for _ in range(N):
        li = list(map(int, input().split()))
        data.append(li)
    cnt = solve(N, data)  # 이 테스트케이스에 대한 정답(최소 전선 길이 합) 계산
    print(f'#{i} {cnt}')  # 출력