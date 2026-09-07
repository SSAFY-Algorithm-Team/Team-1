package huiwon2.week4;
import java.util.Scanner;

public class d2_4836 {
	// 색칠하기(Python to Java)
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++) {
			int N = sc.nextInt();
			
			// 격자 배열 정의
			int[][] grid = new int[10][10];
			
			// 겹치는 그리드 개수
			int count = 0;
			
			// 겹치는 격자 카운트
			for(int i = 0; i < N; i++) {
				// 첫번째 좌표
				int r1 = sc.nextInt();
				int c1 = sc.nextInt();
				
				// 두번째 좌표
				int r2 = sc.nextInt();
				int c2 = sc.nextInt();
				
				// 색깔 번호
				int color = sc.nextInt();
				
				for(int j = r1; j <= r2; j++) {
					for(int k = c1; k <= c2; k++) {
						if(grid[j][k] == 0) {
							grid[j][k] = color;
						}else {
							grid[j][k] += color;
							count += 1;
						}
					}
				}
			}
			System.out.println("#" + test_case + " " + count);
		}
		sc.close();
	}

}