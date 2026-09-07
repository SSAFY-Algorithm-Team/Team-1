#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)



int main(void) {
	int t, m, n, a[3][100];
    scanf("%d", &t);
    for (int i = 1 ; i <= t ; i++) {
        scanf("%d %d", &n, &m);
        for (int j = 0 ; j < n ; j++) {
            for (int k = 0 ; k < m ; k++) {
                scanf("%d", &a[j][k]);
            }
        }
        int max = 0;
        for (int j = 0 ; j < n ; j++) {
            for (int k = 0 ; k < m ;k++) {
                int count = a[j][k];
                if (j-1 >=0) count += a[j-1][k];
                if (k-1 >=0) count+= a[j][k-1];
                if (k+1 < m) count+= a[j][k+1];
                if (j+1 < n) count+= a[j+1][k];
            }
            if (count > max) max = count;
        }
        printf("#%d %d\n", i, max);
    }


	return 0; 
}

