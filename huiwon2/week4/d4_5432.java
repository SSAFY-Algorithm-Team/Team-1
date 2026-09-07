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
	    		 stack.push(char_string[i]);
	         }else{
	             stack.pop();
	             if(char_string[i-1] == '('){
	                 answer += stack.size();
	             }else{
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