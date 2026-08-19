#include <stdio.h>
#include <string.h>

int main(void) {
	int a, b, c1, c2, d[100][100] = { 0 };
	scanf("%d %d", &a, &b);
	for (int i = 0; i < a; i++) {
		scanf("%d %d", &c1, &c2);
		d[c1 - 1][c2 - 1] = 1;
		d[c2 - 1][c1 - 1] = 1;
	}
	
	for (int i = 0; i < b; i++) {
		for (int j = 0; j < b; j++) {
			printf("%d ", d[i][j]);
		}
		printf("\n");
	}

}
