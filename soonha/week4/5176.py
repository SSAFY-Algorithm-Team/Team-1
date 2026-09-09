T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    counter = 1

    def inorder(node):
        global counter
        if node > N: # 존재하지 않는 노드 → 그냥 리턴 (재귀 종료 조건)
            return
        inorder(2 * node)  # 왼쪽 자식부터 끝까지 파고들기
        tree[node] = counter  # 왼쪽을 다 방문했으면 이제 현재 노드에 값 배정
        counter += 1 # 다음 노드를 위해 카운터 하나 증가
        inorder(2 * node + 1)  # 오른쪽 자식 방문

    inorder(1)
    root_val = tree[1] # 루트 노드
    half_val = tree[N // 2] # 문제 조건
    print(f"#{test_case} {root_val} {half_val}")