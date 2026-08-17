T = int(input())
for i in range(1, T + 1):
    N, lo, hi = map(int, input().split()) 
    arr = list(map(int, input().split()))
    arr.sort()

    # 배열 내 경계값 후보 확인
    idx_list = []
    for j in range(1, N):
        if(arr[j - 1] != arr[j]):  # 인접한 두 값이 다른 지점만 경계 가능
            idx_list.append(j)

    min_val = None
    # 3구간으로 나누기
    for x1 in idx_list:
        a = x1  # 하 등급 개수
        if(a < lo or a > hi):
            continue

        # b = x2 - x1, c = N - x2 가 각각 [lo, hi] 범위에 들어오도록 x2 범위 계산
        low_x2 = max(x1 + lo, N - hi)
        high_x2 = min(x1 + hi, N - lo)
        if(low_x2 > high_x2):
            continue

        # idx_list 중 [low_x2, high_x2] 범위에 있는 x2 후보를 순회
        for x2 in idx_list:
            if x2 <= x1:
                continue
            if x2 < low_x2 or x2 > high_x2:
                continue
            b = x2 - x1
            c = N - x2
            diff = max(a, b, c) - min(a, b, c)
            if(min_val == None or diff < min_val):
                min_val = diff

    if(min_val == None):
        print(f'#{i} -1')
    else:
        print(f'#{i} {min_val}')