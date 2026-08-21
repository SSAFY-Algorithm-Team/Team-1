package huiwon2.week1;

public class Fatigue_lv2 {
	// 피로도
	int maxDungeons = 0;
	public static void main(String[] args) {

	}
	public int solution(int k, int[][] dungeons) {
        int answer = -1;
        
        backtrack(k, 0, dungeons);
        
        answer = maxDungeons;
        return answer;
    }
	private void backtrack(int current, int count, int[][]dungeons) {
		boolean[] visited = new boolean[dungeons.length];
		maxDungeons = Math.max(maxDungeons, count);
		
		for(int i = 0; i < dungeons.length; i++) {
			if(!visited[i] && current >= dungeons[i][0]) {
				visited[i] = true;
				backtrack(current - dungeons[i][1], count+1, dungeons);
				visited[i] = false;
			}
		}
	}
}
