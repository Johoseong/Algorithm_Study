import java.io.*;
import java.util.*;

public class Main {

    static int n;
    static int[] alphabet = new int[26];

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(bf.readLine());

        for(int i = 0; i < n; i++) {
            String word = bf.readLine();
            int base = (int) Math.pow(10, word.length() - 1);

            for(int j = 0; j < word.length(); j++) {
                alphabet[word.charAt(j) - 'A'] += base;
                base /= 10;
            }
        }
        Arrays.sort(alphabet);
        int answer = 0;
        for(int i = 25; i >= 0; i--) {
            answer += (alphabet[i] * (i - 16));
        }
        System.out.print(answer);
    }
}