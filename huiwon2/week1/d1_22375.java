package huiwon2.week1;
import java.util.Scanner;
// 스위치 조작
public class d1_22375 {
	
	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++)
		{
			// 스위치 개수
			int N = sc.nextInt();
			
			// 조작 전 스위치 상태
			int[] Ai = new int[N];
			
			// 조작 후 스위치 상태
			int[] Bi = new int[N];
			
			// Ai 입력
			for(int i = 0; i < N; i++) {
				Ai[i] = sc.nextInt();
			}
			// Bi 입력
			for(int i = 0; i < N; i++) {
				Bi[i] = sc.nextInt();
			}
			
			// count(조작 횟수)
			int count = 0;
			
			// Ai와 Bi 비교 -> 다를 시 Ai 값 바꾸기 -> 반복
			for(int i = 0; i < N; i++) {
				if(Ai[i] == Bi[i]) {
					continue;
				}else {
					count++;
					for(int j = i; j < N; j++) {
						if(Ai[j] == 0) {
							Ai[j] = 1;
						}else {
							Ai[j] = 0;
						}
					}
				}
			}
			System.out.println("#" + test_case + " " + count);
 		}
		sc.close();
	}

}
