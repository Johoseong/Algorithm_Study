import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        int m = Integer.parseInt(bf.readLine());
        String str = bf.readLine();
        int answer = 0, cnt = 0;

        for(int i = 1; i < m - 1; i++) {
            if(str.charAt(i - 1) == 'I' && str.charAt(i) == 'O' && str.charAt(i + 1) == 'I') {
                cnt++;
                i++;
                if(n == cnt) {
                    answer++;
                    cnt--;
                }
            }
            else
                cnt = 0;
        }

        System.out.print(answer);
    }
}