#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)

int  a[13][13], max;
void dfs(int idx1, int idx2, int sum, int n) {
	if (idx1 == n || idx2 == n) {
		return;
	}
	sum += a[idx1][idx2];

	if (idx1 == n-1 && idx2 == n-1) {
		if (sum < max) {
			max = sum;
		}
		return;
	}
	
	dfs(idx1+1, idx2, sum, n);
	dfs(idx1, idx2+1, sum, n);
}

int main(void) {
	int t, n;
	scanf("%d", &t);
	
	for (int i = 1; i <= t; i++) {
		scanf("%d", &n);
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < n; k++) {
				scanf("%d", &a[j][k]);
			}
		}
		max = 100000;
		dfs(0, 0, 0, n);
		printf("#%d %d\n", i, max);
	}


}


