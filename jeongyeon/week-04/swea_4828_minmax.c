#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)

int main(void) {
	int t, n, a[1000];
	

	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%d", &n);
		int max = 0;
		int min = 1000001;
		for (int j = 0; j < n; j++) {
			scanf("%d", &a[j]);
			if (a[j] > max) max = a[j];
			if (a[j] < min) min = a[j];
		}
		printf("#%d %d\n", i, max - min);
	}
	return 0;
}

     