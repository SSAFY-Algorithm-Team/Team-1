package huiwon2.week4;
import java.util.Scanner;
import java.util.Stack;

public class d4_5432 {
	// 쇠막대기 자르기
	private static int solution(String string){
		 int answer = 0;
	     char[] char_string = string.toCharArray();

	     // stack 정의
	     Stack<Character> stack = new Stack<>();
	     for (int i = 0; i < char_string.length; i++) {
	    	 if(char_string[i] == '('){
				// 여는 괄호는 계속 push
	    		stack.push(char_string[i]);
	         }else{
	            stack.pop();
	            if(char_string[i-1] == '('){
					// 닫는 괄호를 빼고 난 이전 값이 여는 괄호라면 stack의 사이즈가 쇠막대기가 잘리는 방향
	                answer += stack.size();
	            }else{
					// 그렇지 않으면 잘리는 방향이 아님 -> 이전 값이 닫히는 괄호라 전 값에서 잘렸기 때문에 +1을 해준다.
					// 1개로 나눠지기 때문임
	                answer++;
	            }
	         }
	     }
	     return answer;
	 }
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++) {
			String stick = sc.next();
			
			int result = solution(stick);
			System.out.println("#" + test_case + " " + result);
		}
		sc.close();
	}

}