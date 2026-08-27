package huiwon2.week2;
import java.util.Scanner;
public class d3_5188 {
	// 최소합
	static int N;
	static int minSum = 0;
	static int[][] arr;
	private static void DFS(int row, int column, int sum) {
		// 최소합보다 크면 더 볼 필요가 없음 
		// Pruning(가지치기)
		if(sum >= minSum) {
			return;
		}
		// 이미 끝에 왔을 경우 최소합을 비교 (기존 최소합과 현재 최소합을 update 해야 하는지 확인)
		if(row == N-1 && column == N-1) {
			minSum = Math.min(minSum, sum);
			return;
		}
		
		// 오른쪽으로 이동
		if(column + 1 < N) {
			// sum과 다음 값을 더해서 DFS 호출 
			DFS(row, column + 1, sum + arr[row][column+1]);
		}
		
		// 아래로 이동
		if(row + 1 < N) {
			// sum과 다음 값을 더해서 DFS 호출 
			DFS(row + 1, column, sum + arr[row+1][column]);
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++) {
			N = sc.nextInt();
			
			arr = new int[N][N];
			for(int i = 0; i< N; i++) {
				for(int j = 0; j < N; j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			
			// 반환할 최소합 정의 
			minSum = Integer.MAX_VALUE;
			// 가장 처음값부터 start 
			DFS(0, 0, arr[0][0]);
			System.out.println("#" + test_case + " " + minSum);
		}
		
		sc.close();
	}

}
