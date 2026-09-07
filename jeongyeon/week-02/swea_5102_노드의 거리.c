#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)

int adj[51][51];
int dist[51];
int queue[51];
int front, rear;
int V, E, S, G;

int bfs(int start, int goal) {
	memset(dist, -1, sizeof(dist));
	front = rear = 0;

	dist[start] = 0;
	queue[rear++] = start;

	while (front < rear) {
		int cur = queue[front++];

		if (cur == goal) {
			return dist[cur];
		}

		for (int next = 1; next <= V; next++) {
			if (adj[cur][next] && dist[next] == -1) {
				dist[next] = dist[cur] + 1;
				queue[rear++] = next;
			}
		}
	}
	return -1; // 도달 불가
}

int main(void) {
	int t;
	scanf("%d", &t);

	for (int tc = 1; tc <= t; tc++) {
		scanf("%d %d", &V, &E);
		memset(adj, 0, sizeof(adj));

		for (int i = 0; i < E; i++) {
			int x, y;
			scanf("%d %d", &x, &y);
			adj[x][y] = 1;
			adj[y][x] = 1;
		}

		scanf("%d %d", &S, &G);

		int result = bfs(S, G);
		if (result == -1) result = 0;

		printf("#%d %d\n", tc, result);
	}
	return 0;
}