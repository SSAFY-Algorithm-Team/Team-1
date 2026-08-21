package huiwon2.week1;
import java.util.Scanner;
public class MinSquare_lv1 {
	// 최소 직사각형 찾기
	public static void main(String[] args) {
		// test module
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] sizes = new int[n][2];
		
		for(int i = 0; i < sizes.length; i++) {
			for(int j = 0; j < 2; j++) {
				// sizes[i][0]은 width, sizes[i][1]은 height가 됨
				sizes[i][j] = sc.nextInt();
			}
		}
		System.out.println(solution(sizes));
		sc.close();
	}
	public static int solution(int [][] sizes) {
		int answer = 0;
		// 반환할 크기의 가로/세로 값 선언
		int maxWeight = 0;
		int maxHeight = 0;
		
		// 그 다음부터 완전 탐색 start
		for(int[] size : sizes) {
			// 2-1. 두 길이 중 더 긴 부분을 weight로, 짧은 부분을 height로 통일 
			// *중요 : 어떻게 탐색할지, 탐색 전에 어떻게 데이터를 구성해서 돌릴건지 생각해야됨
			int weight = Math.max(size[0], size[1]);
			int height = Math.min(size[0], size[1]);
			
			// 2-2. 각 최대값 갱신
			maxWeight = Math.max(maxWeight, weight);
			maxHeight = Math.max(maxHeight, height);
		}
		
		answer = maxWeight * maxHeight;
		return answer;
	}

}
