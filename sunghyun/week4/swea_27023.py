from collections import deque

T = int(input())
for tc in range(1, T + 1):
    M = int(input())
    ops = list(map(int, input().split()))

    q = deque()
    num = 0          
    called = []      

    for op in ops:
        if op == 1:             
            num += 1
            q.append(num)
        else:
            called.append(q.popleft())

    print(f'#{tc}', *called)