# [문제]
# 하나의 정점 여러개 간선, 양방향
# 방문할 수 있는 정점 여러개일땐,
# 정점 번호가 작은 것 먼저 방문
# 더이상 방문할 수 있는 점 없으면 종료
# 정점 번호는 1번~n번
# 다음 m개의 줄에 간선의 정보가 주어짐- 간선이 연결하는 두점 번호

# [출력]
# 탐색을 시작한 정점부터 차례로 방문한 정점 순서대로 출력

# 정점 개수, 간선 개수, 탐색시작정점 번호
n, m, v = map(int, input().split())

# 스택+인접리스트로 풀기

# 인접리스트 먼저 구현
adj_list = [[] for _ in range(n+1)]

for _ in range(m):  # 정점이 아니라 간선 개수만큼 반복
    start, end = map(int, input().split())
    adj_list[start].append(end)
    adj_list[end].append(start)

visited = []
stack = [v]

while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current)
        for des in adj_list[current]:
            if des not in visited:
                stack.append(des)
        stack.sort(reverse=True)    # 내림차순으로 정렬
        # 내림차 순으로 정렬해야 작은 노드부터 탐색할 수 있음

print(*visited)