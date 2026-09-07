#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)

int main(void) {
	int t, n, a[30][5];

	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		int b[10][10] = { 0 };
		scanf("%d", &n);
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < 5; k++) {
				scanf("%d", &a[j][k]);
			}
		}
		int count = 0;
		for (int j = 0; j < n; j++) {
			for (int k = a[j][0]; k <= a[j][2]; k++) {
				for (int l = a[j][1]; l <= a[j][3]; l++) {
					if (b[k][l] == 0) {
						b[k][l] = a[j][4];
					}
					else if (b[k][l] == 1) {
						if (a[j][4] == 1) continue;
						else if (a[j][4] == 2) {
							count++;
							b[k][l] = 3;
						}
					}
					else if (b[k][l] == 2) {
						if (a[j][4] == 2) continue;
						else if (a[j][4] == 1) {
							count++;
							b[k][l] = 3;
						}
					}
					else if (b[k][l] == 3) {
						continue;
					}
				}
			}
		}
		printf("#%d %d\n", i, count);

	}
	return 0;
}

