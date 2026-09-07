package huiwon2.week4;
import java.util.Scanner;

public class d3_3499 {
	// 퍼펙트 셔플
	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++) {
			// 자연수
			int N = sc.nextInt();
			
			// 자연수 N이 홀수인지 짝수인지 따라 A배열과 B배열 길이를 다르게 가져간다.
			// 퍼펙트 셔플의 첫번째 배열 길이
			int a_len = 0;
			// 퍼펙트 셔플의 두번째 배열 길이
			int b_len = 0;
			
			if(N % 2 == 1) {
				a_len = N / 2 + 1;
				b_len = N / 2;
			}else {
				a_len = N / 2;
				b_len = N / 2;
			}
			
			// 문자열 배열 A/B 선언
			String[] A = new String[a_len];
			String[] B = new String[b_len];
			
			for(int i = 0; i < A.length; i++) {
				A[i] = sc.next();
			}
			for(int i = 0; i < B.length; i++) {
				B[i] = sc.next();
			}
			
			// 새롭게 셔플해서 합칠 배열 선언(길이는 N)
			String[] shuffle = new String[N];
			
			// shuffle 배열에 데이터 넣어주기 + 출력
			System.out.print("#" + test_case + " ");
			for(int i = 0; i < shuffle.length; i++) {
				// i가 짝수이다 -> A 배열의 값이 들어온다
				if(i % 2 == 0) {
					shuffle[i] = A[i / 2];
				}
				// i가 홀수이다 -> B 배열의 값이 들어온다
				else {
					shuffle[i] = B[i / 2];
				}
				
				System.out.print(shuffle[i] + " ");
			}
			System.out.println();
			
		}
		sc.close();
	}

}