class Solution {
    static int answer;
    public void dfs(int index, int[] numbers, int target, int cur) {
        if(index == numbers.length - 1) {
            if(cur == target)
                answer++;
            return;
        }
        dfs(index + 1, numbers, target, cur + numbers[index + 1]);
        dfs(index + 1, numbers, target, cur - numbers[index + 1]);
    }

    public int solution(int[] numbers, int target) {
        answer = 0;
        dfs(-1, numbers, target, 0);
        return answer;
    }
}