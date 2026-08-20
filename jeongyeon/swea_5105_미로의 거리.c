#include <stdio.h>
#include <string.h>

int a[101][101];
int visited[101][101];
int n;
int sx, sy, ex, ey;

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

typedef struct { int x, y; } Point;
Point queue[10001];
int front, rear;

int bfs() {
    front = rear = 0;
    memset(visited, 0, sizeof(visited));

    visited[sx][sy] = 1;
    queue[rear++] = (Point){sx, sy};

    while (front < rear) {
        Point cur = queue[front++];

        if (cur.x == ex && cur.y == ey) {
            return visited[cur.x][cur.y];
        }

        for (int d = 0; d < 4; d++) {
            int nx = cur.x + dx[d];
            int ny = cur.y + dy[d];

            if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
            if (a[nx][ny] == 1) continue;       // 벽
            if (visited[nx][ny]) continue;       // 이미 방문

            visited[nx][ny] = visited[cur.x][cur.y] + 1;
            queue[rear++] = (Point){nx, ny};
        }
    }
    return 0; // 경로 없음
}

int main(void) {
    int t;
    scanf("%d", &t);

    for (int i = 1; i <= t; i++) {
        scanf("%d", &n);
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                scanf("%d", &a[j][k]);
                if (a[j][k] == 2) { sx = j; sy = k; }
                else if (a[j][k] == 3) { ex = j; ey = k; }
            }
        }
        printf("#%d %d\n", i, bfs());
    }
    return 0;
}