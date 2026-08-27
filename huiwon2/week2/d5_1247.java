package huiwon2.week2;

import java.util.Scanner;

public class d5_1247 {
	// 최적 경로(공통)
	static int N;
	static int[][] points;
	static boolean[] checked;
	static int minDistance;
	private static void DFS(int current, int count, int distanceSum) {
		// Pruning
		if(distanceSum >= minDistance) {
			return;
		}
		// Pruning(count가 n과 같을 때)
		if(count == N) {
			// 마지막 위치에서 집(1)으로 가는 거리가 필요했음(내가 마주친 오류)
			// 이상한 N+1로 가버림..
			int finalDistance = distanceSum + getDistance(current, 1);
			minDistance = Math.min(minDistance, finalDistance);
			return;
		}
		// 순회
		for(int i = 2; i < N + 2; i++) {
			if(!checked[i]) {
				checked[i] = true;
				int next = getDistance(current, i);
				DFS(i, count+1, distanceSum + next);
				// backtracking
				checked[i] = false;
			}
		}
	}
	// 두 좌표 사이의 거리
	static int getDistance(int point1, int point2) {
		// abs(x1 - x2) + abs(y1 - y2) <- 문제에서 제공한 거리
		return Math.abs(points[point1][0] - points[point2][0]) + Math.abs(points[point1][1] - points[point2][1]);
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++) {
			N = sc.nextInt();
			// 회사 좌표와 집 좌표, N개의 좌표 필요
			points = new int[N + 2][2];
			checked = new boolean[N + 2];
			//회사 좌표
			points[0][0] = sc.nextInt();
			points[0][1] = sc.nextInt();
			
			// 집 좌표
			points[1][0] = sc.nextInt();
			points[1][1] = sc.nextInt();
			
			for(int i = 2; i < N+2; i++) {
				points[i][0] = sc.nextInt();
				points[i][1] = sc.nextInt();
			}
			
			minDistance = Integer.MAX_VALUE;
      // DFS 호출 (현재 위치, 고객 방문 수, 현재 sum(한번도 가지 않았으니 0))
			DFS(0, 0, 0);
			System.out.println("#" + test_case + " " + minDistance);
		}
		sc.close();
	}

}