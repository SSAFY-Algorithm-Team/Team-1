package huiwon2.week1;

import java.util.Scanner;
import java.util.HashSet;
import java.util.Set;
// 프로그래머스 - 소수찾기 Level2
public class PrimeNumber_lv2 {
	// numbers를 이용해 가능한 숫자를 담는 HashSet 선언(전역 변수)
	static Set<Integer> numberSet = new HashSet<>();
	public static int solution(String numbers) {
		int answer = 0;
		
		// String으로 받은 numbers를 끊어서 자릿수 보관 배열 생성 
		int[] numbers_arr = new int[numbers.length()];
		for(int i = 0; i < numbers_arr.length; i++) {
			numbers_arr[i] = numbers.charAt(i) - '0';
		}
		
		// 방문 여부 visited
		boolean[] visited = new boolean[numbers.length()];
		
		// 순열 생성 함수 호출 
		generateCombinations("", numbers, visited);
		// 결과 출력 
        // System.out.println("만들 수 있는 모든 숫자: " + numberSet);
		
		// 배열의 값으로 소수 판별
		for(int num : numberSet){
			if(isPrime(num)) {
				// 소수일 때 answer++
				answer ++;
			}
		}
		
		return answer;
	}
	
	// 완전탐색 - 중복 없는 숫자 배열 반환 메서드
	private static void generateCombinations(String current, String numbers, boolean[] visited){
		if(!current.isEmpty()) {
			numberSet.add(Integer.parseInt(current));
			// add가 어떤 방식으로 되는지 확인
			System.out.println(numberSet);
		}
		
		// 모든 자릿수에 재귀 호출 
		for(int i = 0; i < numbers.length(); i++) {
			if(!visited[i]) {
				visited[i] = true;
				generateCombinations(current + numbers.charAt(i), numbers, visited);
				visited[i] = false;
			}
		}
	}
	
	// 소수판별 - isPrime
	public static boolean isPrime(int num) {
		if(num < 2) {
			return false;
		}
		// 원래 자기자신 -1 까지 나눠지는 값으로 판별
		// 소수가 아니라면 제곱근 이하에 최소한 나눠지는 값이 하나 이상 존재(설명)
		// 시간 절약을 위해 제곱근으로 계산 
		for(int i = 2; i * i<= num; i++) {
			if(num % i == 0) {
				return false;
			}
		}
		return true;
	}
	// Main Test 
	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(System.in);
		String num = sc.next();
		
		System.out.print(solution(num));
		sc.close();
	}
}
