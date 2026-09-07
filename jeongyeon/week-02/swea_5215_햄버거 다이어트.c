#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)

int a[21][21];
int max, n, l;
void dfs(int idx, int score, int kal) {
	if (kal > l) {
		return;
	}
	if (idx == n) {
		if (score > max) max = score;
		return;
	}

	dfs(idx + 1, score + a[idx][0], kal + a[idx][1]);
	dfs(idx + 1, score, kal);
}

int main(void) {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%d %d", &n, &l);
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < 2; k++) {
				scanf("%d", &a[j][k]);
			}
		}
		max = 0;
		dfs(0, 0, 0);

		printf("#%d %d\n", i, max);
	}
	
}	

