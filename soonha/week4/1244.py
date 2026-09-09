T = int(input()) # 테스트케이스
for test_case in range(1, T + 1):
    num, change = input().split() # 숫자판의 정보 num, 교환 횟수 change
    change = int(change) # change 정수화
    arr = [] # 숫자판을 기록하기 위한 리스트
    for i in num: # 숫자판 저장
        arr.append(int(i))

    N = len(arr) # 숫자판의 길이

    max_val = -1 # 최댓값
    visited = set()  # (배열 상태, 남은 교환 가능한 횟수)를 저장해 중복 탐색 방지

    def dfs(cnt):
        global max_val
        if cnt == change:  # 교환을 정해진 횟수만큼 다 했다면
            val = int(''.join(map(str, arr)))
            if val > max_val:
                max_val = val
            return

        state = (tuple(arr), cnt)
        if state in visited:  # 이미 이 상태를 탐색했다면 스킵
            return
        visited.add(state)

        for i in range(N):
            for j in range(i + 1, N):  # 서로 다른 두 자리를 모두 선택
                arr[i], arr[j] = arr[j], arr[i]  # 교환
                dfs(cnt + 1) # DFS 재귀 실행
                arr[i], arr[j] = arr[j], arr[i]  # 백트래킹(원상복구)

    dfs(0) # DFS 실행

    print(f'#{test_case} {max_val}') # 출력