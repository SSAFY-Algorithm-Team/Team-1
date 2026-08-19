package huiwon2.week2;
import java.util.Scanner;

public class Java_1397 {
	// 코더스패스 양방향 인접 행렬 출력
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// 간선 
		int A = sc.nextInt();
		// 정점의 수 
		int B = sc.nextInt();
		// 출력할 인접행렬
		int[][] graph = new int[B + 1][B + 1];
		
		// 간선 입력 받기 + 인접행렬 표시 
		for(int i = 0; i < A; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			// 인접행렬(무방향 그래프) 양방향으로 1 처리 
			graph[a][b] = 1;
			graph[b][a] = 1;
		}
		
		// 행렬 출력
		for(int i = 1; i < graph.length; i++) {
			for(int j = 1; j < graph[i].length; j++) {
				System.out.print(graph[i][j]);
			}
			System.out.println();
		}
		sc.close();
	}

}