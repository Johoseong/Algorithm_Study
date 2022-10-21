import java.util.*;

public class Main {
    static int arr[], lDP[], rDP[];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        arr = new int[n];
        lDP = new int[n];
        rDP = new int[n];

        for(int i = 0; i < n; i++)
            arr[i] = sc.nextInt();

        for(int i = 0; i < n; i++) {
            lDP[i] = 1;
            rDP[n - i - 1] = 1;
            for(int j = 0; j <= i; j++) {
                if(arr[j] < arr[i]) {
                    lDP[i] = Math.max(lDP[i], lDP[j] + 1);
                }
            }
            for(int j = n - 1; j >= n - i - 1; j--) {
                if(arr[j] < arr[n - i - 1])
                    rDP[n - i - 1] = Math.max(rDP[n - i - 1], rDP[j] + 1);
            }
        }
        int answer = 1, tmp = 0;
        for(int i = 0; i < n; i++) {
            tmp = lDP[i];
            for(int j = i + 1; j < n; j++) {
                if(arr[i] > arr[j])
                    tmp = Math.max(tmp, lDP[i] + rDP[j]);
            }
            answer = Math.max(answer, tmp);
        }
        System.out.print(answer);
    }
}
