import java.util.Scanner;
public class project11053 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int A = scan.nextInt();
		int seq[] = new int[A]; //수열
		int dp[] = new int[A]; //메모이제이션
		int max;
		for(int i = 0; i < A; i++)
			seq[i] = scan.nextInt();
		
		for(int i = 0; i < A; i++) {
			dp[i] = 1; max = 1;
			for(int j = 0 ;j < i; j++) {
				
				if(seq[i] > seq[j]){
					/*if(dp[i]<dp[j]+1)
				 * dp[i] = dp[j]+1; //요건 뭔가 생각 못해낼 거 같아서..
				 */
					if(max < dp[j])
						max = dp[j];
					dp[i] = max+1;					
				}
			}
		}
		max = -1;
		for(int i = 0 ;i < A; i++) {
			if(max<dp[i])
				max = dp[i];
		}
		
		System.out.println(max);
	}
}

/* - seq[] 배열에 수열 값을 저장한다
 * - dp[] 배열은 각 수열 위치에서의  증가하는 수열 갯수를 입력
 * - seq[i]>seq[j]인 경우 + 이전의 dp길이중에 제일 긴 경우 2가지 조건을 고려해서 dp[i]값 지정
 * 
 * */
 
