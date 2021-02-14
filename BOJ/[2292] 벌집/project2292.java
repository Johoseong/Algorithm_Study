package baekjoon;
import java.util.Scanner;
public class project2292 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		int i = 6;
		int count = 1;
		while(true) {
			
			if(N<=1)
				break;
			
			N = N-i*count;
			count++;
							
					}
		System.out.println(count);
		
	}
		
	}
