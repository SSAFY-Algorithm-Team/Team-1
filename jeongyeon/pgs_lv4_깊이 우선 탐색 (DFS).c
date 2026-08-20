#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)

int adj[1001][1001];  // 인접 행렬
int visited[1001];
int n, m, v;
void dfs(int cur) {
	visited[cur] = 1;
	printf("%d ", cur);

	for (int next = 1; next <= n; next++) {
		if (adj[cur][next] && !visited[next]) {
			dfs(next);
		}
	}
}

int main(void) {
	scanf("%d %d %d", &n, &m, &v); //정점, 간선, 탐색 시작할 정점 번호
	for (int i = 0; i < m; i++) {
		int x, y;
		scanf("%d %d", &x, &y);
		adj[x][y] = 1;
		adj[y][x] = 1;
	}
	dfs(v);
	return 0; 
}

