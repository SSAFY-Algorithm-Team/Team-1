from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[-1] * 102 for _ in range(102)]
    for x1, y1, x2, y2 in rectangle :
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for x in range(x1, x2+1) :
            for y in range(y1, y2 + 1) :
                if x1 <x <x2 and y1 < y < y2 :
                    board[x][y] = 0
                elif board[x][y] != 0 :
                    board[x][y] = 1
    sx, sy, ex, ey = characterX *2, characterY*2, itemX*2, itemY*2
    q = deque([(sx, sy)])
    dist = [[-1] * 102 for _ in range(102)]
    dist[sx][sy] = 0
    while q :
        x, y = q.popleft()
        if x == ex and y == ey :
            return dist[x][y] // 2
        for dx, dy in ((0, 1), (0,-1), (1, 0), (-1, 0)) :
            nx = x + dx
            ny = y + dy
            if board[nx][ny] == 1 and dist[nx][ny] == -1 :
                dist[nx][ny] = dist[x][y]+1
                q.append((nx, ny))
        