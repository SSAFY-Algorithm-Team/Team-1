#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)

int adj[101][101];
int visited[101];
int n, m;
void dfs(int cur) {
	visited[cur] = 1;
	for (int next = 1; next <= n; next++) {
		if (adj[cur][next] && !visited[next]) {
			dfs(next);
		}
	}
}

int main(void) {
	scanf("%d %d", &n, &m);
	for (int i = 0; i < m; i++) {
		int x, y;
		scanf("%d %d", &x, &y);
		adj[x][y] = 1;
		adj[y][x] = 1;
	}

	int count = 0;
	for (int i = 1; i <= n; i++) {
		if (!visited[i]) {
			dfs(i);
			count++;
		}
	}

	printf("%d\n", count);
	return 0;
}