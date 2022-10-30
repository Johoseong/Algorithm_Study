import java.io.*;
import java.util.*;

public class Main {

    static int n, k, dp[];

    static void init() {
        dp = new int[k + 1];
        for(int i = 0; i <= k; i++)
            dp[i] = Integer.MAX_VALUE - 1;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        init();
        int coin;

        for(int i = 0; i < n; i++) {
            coin = Integer.parseInt(bf.readLine());
            if(coin > k)
                continue;
            dp[coin] = 1;
            for(int j = coin + 1; j <= k; j++) {
                dp[j] = Math.min(dp[j], dp[j - coin] + 1);
            }
        }
        if(dp[k] == Integer.MAX_VALUE - 1)
            System.out.print(-1);
        else
            System.out.print(dp[k]);
    }
}