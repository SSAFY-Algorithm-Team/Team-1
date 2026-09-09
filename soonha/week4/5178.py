T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split()) # 노드 갯수 N, 리프 노드 개수 M, 출력할 노드 번호 L
    tree = [0] * (N + 1)
    for i in range(M): # 리프 노드 삽입
        node_num, num = map(int, input().split())
        tree[node_num] = num

    def sum(idx):
        if idx > N: # 존재하지 않는 노드 -> 0으로 취급
            return 0
        if tree[idx] != 0: # 이미 값이 있으면 그대로 반환
            return tree[idx]
        left = sum(idx * 2)
        right = sum(idx * 2 + 1)
        tree[idx] = left + right
        return tree[idx]

    sum(1) # 합을 구하는 함수 실행
    print(f'#{test_case} {tree[L]}')