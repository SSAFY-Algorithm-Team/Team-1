T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split()) # 재료의 수 N, 제한 칼로리 L
    items = [] # 재료에 대한 정보를 저장할 리스트
    for _ in range(N): 
        taste, kcal = map(int, input().split()) # 맛 점수 taste, 칼로리 kcal
        items.append((taste, kcal))

    best = 0 # 조건을 충족하는 조합 중 최대 맛 점수

    def dfs(i, taste_sum, cal_sum):
        global best
        if cal_sum > L: # 칼로리 제한 초과 시 가지치기
            return
        if taste_sum > best: # 조건 만족 시 최댓값 갱신
            best = taste_sum
        if i == N: # 모든 재료를 다 살펴보면 종료
            return
        dfs(i + 1, taste_sum + items[i][0], cal_sum + items[i][1]) # i번째 재료 선택
        dfs(i + 1, taste_sum, cal_sum) # i번째 재료 미선택

    dfs(0, 0, 0)
    print(f'#{test_case} {best}')