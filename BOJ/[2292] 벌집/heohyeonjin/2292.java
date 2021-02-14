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

/*규칙   -최소 개수의 방을 지나는 횟수가 1은 1번, 2~7은 2번, 8~19는 3번, 20~37은 4번
 *    -1을 제외하고 숫자 범위가 6개,12개,18개...
 *횟수만 알면 되므로 N값에서 6,12,18순으로 뺄셈을 해주어 N이 1보다 작거나 같으면 종료 하도록 한다
 */
  
