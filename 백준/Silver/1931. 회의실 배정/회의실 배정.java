import java.io.*;
import java.util.*;

public class Main {

    static int arr[][];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        arr = new int[n][2];

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr, (o1, o2) -> {
            if(o1[1] == o2[1])
                return Integer.compare(o1[0], o2[0]);
            else
                return Integer.compare(o1[1], o2[1]);
        });

        int start = arr[0][0], answer = 0;
        for(int i = 0; i < n; i++) {
            if(arr[i][0] >= start) {
                answer += 1;
                start = arr[i][1];
            }
        }

        System.out.print(answer);
    }
}