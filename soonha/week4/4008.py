from itertools import permutations
T = int(input()) # 테스트케이스 T
for test_case in range(1, T + 1):
    N = int(input()) # 숫자의 갯수 N
    op_cnt = list(map(int, input().split())) # [+, -, *, / 갯수]
    nums = list(map(int, input().split()))

    max_val, min_val = -10 ** 9, 10 ** 9 # 문제 조건을 고려 최댓값, 최솟값에 대한 초기값 설정

    def div(a, b): # 나눗셈
        q = abs(a) // b
        if(a < 0):
            return -q
        else:
            return q

    def dfs(idx, val):
        global max_val, min_val
        if idx == N: # 숫자를 다 사용했다면
            if val > max_val: # 최댓값 비교
                max_val = val
            if val < min_val: # 최솟값 비교
                min_val = val
            return
        for operator in range(4): # 0: +, 1: -, 2: *, 3: /
            if op_cnt[operator] > 0: # 연산자 카드가 남아있다면
                op_cnt[operator] -= 1 # 해당 연산자 카드 사용
                if operator == 0: # '+'
                    new_val = val + nums[idx]
                elif operator == 1: # '-'
                    new_val = val - nums[idx]
                elif operator == 2: # '*'
                    new_val = val * nums[idx]
                elif operator == 3: # '/'
                    new_val = div(val, nums[idx])
                dfs(idx + 1, new_val) # 다음 idx로
                op_cnt[operator] += 1 # 백트래킹

    dfs(1, nums[0]) # idx: 첫 번째에서 시작, val값을 0번째 숫자 값으로
    result = max_val - min_val
    print(f'#{test_case} {result}') # 출력