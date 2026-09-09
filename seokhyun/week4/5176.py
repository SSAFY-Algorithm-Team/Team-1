# SWEA 5176 이진탐색
import sys
sys.stdin = open("input.txt", "r")
# 조건 체크 절차
# 1. 존재하는 노드인가? N의 범위 안에 있는가?
# 2. leaf 노드인가?
# 3. leaf 노드가 아니라면 좌우의 값이 있는가 체크 후 없는 값 순회
# 4. leaf 노드가 아니라면 count값 할당

# BST의 구조를 만드려면 중위 순회처럼 접근하면 된다.
def make_bst(BST, idx):
    global count
    left = idx * 2
    rigth = idx * 2 + 1

    # 존재하는 노드인가?
    if idx >  N:
        return 

    # 왼쪽 자식이 존재하는가?
    if left <= N:
        # 왼쪽 자식 값이 있는가?
        if BST[left] == 0:
            make_bst(BST, left)

    # 현재 idx에 count 값 할당.
    BST[idx] = count
    count += 1

    # 오른쪽 자식이 존재하는가?
    if rigth <= N:
        # 오른쪽 자식 값이 있는가?
        if BST[rigth] == 0:
            make_bst(BST, rigth)

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    BST = [0] * (N+1)
    count = 1

    make_bst(BST, 1)

    print(f"#{test_case} {BST[1]} {BST[N//2]}")