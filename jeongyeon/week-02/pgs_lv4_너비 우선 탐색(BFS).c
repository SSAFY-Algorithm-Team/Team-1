#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)


int adj[1001][1001];
int visited[1001];
int queue[1001];
int front, rear;
int n, m, v;

void bfs(int start) {
	front = rear = 0;
	visited[start] = 1;
	queue[rear++] = start;

	while (front < rear) {
		int cur = queue[front++];
		printf("%d ", cur);

		for (int next = 1; next <= n; next++) {
			if (adj[cur][next] && !visited[next]) {
				visited[next] = 1;
				queue[rear++] = next;
			}
		}
	}
}

int main(void) {
	scanf("%d %d %d", &n, &m, &v);

	for (int i = 0; i < m; i++) {
		int x, y;
		scanf("%d %d", &x, &y);
		adj[x][y] = 1;
		adj[y][x] = 1;
	}

	bfs(v);
	return 0;
}