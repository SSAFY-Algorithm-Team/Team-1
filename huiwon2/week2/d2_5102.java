package huiwon2.week2;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class d2_5102 {
  // 노드의 거리 
	static ArrayList<ArrayList<Integer>> graph;
	static int[] distance;
	static boolean[] checked;
	// BFS
	private static int BFS(int start, int end) {
		// start == end
		if(start == end) {
			return 0;
		}
		Queue<Integer> queue = new LinkedList<>();
		checked[start] = true;
		distance[start] = 0;
		queue.offer(start);
		
		while(!queue.isEmpty()) {
			int current = queue.poll();
			for(int next : graph.get(current)) {
				if(!checked[next]) {
					checked[next] = true;
					distance[next] = distance[current] + 1;
					
					// 목적지 도달 
					if(next == end) {
						return distance[next];
					}
					
					queue.offer(next);
				}
			}
		}
		return -1;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++)
		{
			// node
			int N = sc.nextInt();
			// edge
			int E = sc.nextInt();
			
			graph = new ArrayList<ArrayList<Integer>>();
			for(int i = 0; i < N+1; i++) {
				graph.add(new ArrayList<Integer>());
			}
			distance = new int[N+1];
			checked = new boolean[N+1];
			
			for(int i = 0; i < E; i++) {
				int a = sc.nextInt();
				int b = sc.nextInt();
				graph.get(a).add(b);
				graph.get(b).add(a);
			}
			
			// start and end
			int S = sc.nextInt();
			int G = sc.nextInt();
			
			// S => G까지 가는 최소 distance 반환(BFS) 
			int answer = BFS(S, G);
			
			System.out.println("#" + test_case + " " + answer);
		}
		sc.close();
	}
}
