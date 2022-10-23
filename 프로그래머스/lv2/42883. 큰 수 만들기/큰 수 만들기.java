class Solution {
    public String solution(String number, int k) {
        StringBuilder answer = new StringBuilder();
        char curMax;
        int nextIndex = -1;

        for(int i = 0; i < number.length() - k; i++) {
            curMax = '0';
            for(int j = nextIndex + 1; j <= k + answer.length(); j++) {
                if(number.charAt(j) > curMax) {
                    curMax = number.charAt(j);
                    nextIndex = j;
                }
            }
            answer.append(curMax);
        }

        return answer.toString();
    }
}