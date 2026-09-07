#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)

int main(void) {
	int t, n, a[50][50];
	char b[60];

	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%d", &n);
		for (int j = 0; j < n; j++) {
			scanf(" %s", b);
			for (int k = 0; k < n; k++) {
				a[j][k] = b[k] - '0';
			}
		}
		int count = 0;
		int c = 0;
		int v = 0;
		for (int j = 0; j <n; j++) {
			for (int k = n/2-c; k <= n/2+c; k++) {
				count += a[j][k];

			}
			if (c == n / 2) v = 1;
			if (v == 0) c++;
			else c--;

		}

		printf("#%d %d\n", i, count);

	}
	return 0;
}

