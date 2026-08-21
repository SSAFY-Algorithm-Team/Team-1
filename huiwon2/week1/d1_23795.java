package huiwon2.week1;
import java.util.Scanner;
// 우주 괴물
public class d1_23795 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++)
		{
			// 칸 수 입력
			int N = sc.nextInt();
			
			// N*N 배열 입력
			int[][] array = new int[N][N];
			for(int i = 0; i < N; i++) {
				for(int j = 0; j < N; j++) {
					array[i][j] = sc.nextInt();
				}
			}
			
			// 안전한 칸 count
			int count = 0;
			
			// 0은 빈 칸, 1은 벽, 2는 괴물
			// 1) 괴물 찾기(index 저장)
			int i_index = -1;
			int j_index = -1;
			
			outer:
			for(int i = 0; i < array.length; i++) {
				for(int j = 0; j < array[i].length; j++) {
					if(array[i][j] == 2) {
						 i_index = i;
				         j_index = j;
				         break outer;
					}
				}
			}
			
			// 2) 괴물 위치를 기준으로 0 -> 2로 수정
			// 상/하/좌/우 방향 배열
			int[] dx = {-1, 1, 0, 0};
			int[] dy = {0, 0, -1, 1};
			
			// 상/하/좌/우 확장
			for(int d = 0; d < 4; d++) {
				int next_i = i_index + dx[d];
				int next_j = j_index + dy[d];
				
				// 범위를 벗어나지 않고, 벽을 만나지 않을 때까지 직진
				while(next_i >= 0 && next_i < array.length && next_j >= 0 && next_j < array.length) {
					if(array[next_i][next_j] == 1) {
						break;
					}
					else if(array[next_i][next_j] == 0) {
						array[next_i][next_j] = 2;
					}
					
					// 한칸 더 이동
					next_i += dx[d];
					next_j += dy[d];
				}
			}
			
			// 3) 전체 배열에서 0값을 count
			for(int i = 0; i < array.length; i++) {
				for(int j = 0; j < array[i].length; j++) {
					if(array[i][j] == 0) {
						 count ++;
					}
				}
			}
			System.out.println("#" + test_case + " " + count);
		}
		sc.close();
	}

}
