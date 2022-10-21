import java.util.*;
class Solution {
    public int solution(int N, int number) {
        int cur = 0;
        Set<Integer> dp[] = new Set[9];

        for (int i = 0; i < 9; i++)
            dp[i] = new HashSet<>();

        for (int i = 1; i < 9; i++) {
            cur += (Math.pow(10, i - 1) * N);
            dp[i].add(cur);

            for (int j = 1; j < i; j++) {
                for (int jNum: dp[j]) {
                    for (int kNum: dp[i - j]) {
                        dp[i].add(jNum + kNum);
                        dp[i].add(jNum - kNum);
                        dp[i].add(jNum * kNum);
                        if (kNum != 0)
                            dp[i].add(jNum / kNum);
                    }
                }
            }
            if (dp[i].contains(number))
                return i;
        }
        return -1;
    }
}