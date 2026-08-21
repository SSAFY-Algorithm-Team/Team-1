package huiwon2.week1;
import java.util.Scanner;
//import java.io.FileInputStream;
// 길이가 m인 회문 찾기
public class d1_21936 {

	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();
		
		for(int test_case = 1; test_case <= T; test_case++)
		{
			// 문자열 길이 입력
			int N = sc.nextInt();
			
			// 회문 길이 입력
			int M = sc.nextInt();
			
			// 문자열 입력
			String s = sc.next();
			
			if(s.length() > N) {
				s = s.substring(0, N);
			}
			
			// 반환 문자열
			String result = "";
			
			// 회문 찾기 start
			for(int i = 0; i < s.length(); i++) {
				if(!result.isEmpty()) {
					break;
				}
				// substring 생성(주의 : 길이 제한)
				if(i + M <= s.length()) {
					String sub = s.substring(i, i + M);
					int left = 0;
					int right = sub.length() - 1;
					// 회문 비교 start
					while(result.length() < sub.length()) {
						if(sub.charAt(left) == sub.charAt(right)) {
							result += sub.charAt(left);
						}else {
							break;
						}
						left++;
						right--;
					}
				}
			}
			
			// 반환 문자열이 비어있다면 -> none 처리
			if(result.isEmpty()) {
				result += "NONE";
			}
			System.out.println("#" + test_case + " " + result);
		}
		sc.close();
	}

}
