package huiwon2.week1;
import java.util.Scanner;
import java.util.Arrays;
public class d2_26059 {
	// 과일 등급 분류
	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(System.in);
		int T;
        T=sc.nextInt();
        
        for(int test_case = 1; test_case <= T; test_case++)
        {
        	// 과일의 개수
        	int N = sc.nextInt();
        	// 최소 개수
        	int lo = sc.nextInt();
        	// 최대 개수
        	int hi = sc.nextInt();
        	
        	// 차이(return)
        	int min_diff = Integer.MAX_VALUE;
        	
        	// 과일 배열 입력
        	int[] fruits = new int[N];
        	for(int i = 0; i < N; i++) {
        		fruits[i] = sc.nextInt();
        	}
        	
        	// 과일 배열 오름차순 정렬
        	Arrays.sort(fruits);
        	
        	// 조건에 부합하는 K1과 K2 경계값 찾기
        	for(int i = 0; i < N - 2; i++) {
        		int K1 = fruits[i + 1];
        		for(int j = 1; j < N - 1; j++) {
        			int K2 = fruits[j + 1];
        			// 등급(상/중/하)별 개수 선언
                	int premium = 0;
                	int standard = 0;
                	int economy = 0;
                	for(int f : fruits) {
                		if(f < K1) {
                			economy++;
                		}else if(f < K2) {
                			standard++;
                		}else {
                			premium++;
                		}
                	}
                	if(lo <= economy && economy <= hi 
                		&& lo <= standard && standard <= hi 
                		&& lo <= premium && premium <= hi ) {
                		// 가장 많은 등급의 수 - 가장 적은 등급의 수
                		int max = Math.max(economy, Math.max(standard, premium));
                		int min = Math.min(economy, Math.min(standard, premium));
                		int diff = max - min;
                		// 최솟값 갱신
                		min_diff = Math.min(min_diff, diff);
                	}
        		}
        	}
        	
        	System.out.println("#" + test_case + " " + min_diff);
        }
        
		sc.close();
	}

}
