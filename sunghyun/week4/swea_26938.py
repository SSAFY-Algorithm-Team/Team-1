from collections import deque

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    nums = list(map(int, input().split()))

    children = [[] for _ in range(E + 2)]   
    for i in range(E):
        p, c = nums[i * 2], nums[i * 2 + 1]
        if c != 0:                      
            children[p].append(c)

    cnt = 0
    q = deque([N])
    while q:
        node = q.popleft()
        cnt += 1
        q.extend(children[node])

    print(f'#{tc} {cnt}')