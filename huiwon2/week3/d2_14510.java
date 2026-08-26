package huiwon2.week3;

import java.util.Scanner;

public class d2_14510 {
  // 나무 높이
	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int N = sc.nextInt();
			int[] tree = new int[N];
			int tree_max = 0;
			for(int i = 0; i < N; i++) {
				tree[i] = sc.nextInt();
				// 가장 높은 트리의 값 반환 
				if(tree_max <= tree[i]) {
					tree_max = tree[i];
				}
			}
			// 짝수일, 홀수일 선언
			int odd = 0; // 필요한 +1(짝수)
			int even = 0; // 필요한 +2(홀수)
			
			for(int i = 0; i < N; i++) {
				// 차이값 계산 
				int diff = tree_max - tree[i];
				// 차이 중 odd로 계산 하는 일자가 빠른지, even으로 계산하는 일자가 빠른지 확인
				odd += diff % 2;
				even += diff / 2;
			}
			
			while(even > odd + 1) {
				even -= 1;
				odd += 2;
			}
			
			int result = 0;
			if(odd > even) {
				result = odd * 2 - 1;
			}else {
				result = even * 2;
			}
			
			System.out.println("#" + test_case + " " + result);
		}
		sc.close();
	}
}
