/*문제풀이핵심:
DP배열에 자신을 포함한 증가하는 수열의 길이 값을 저장한다.
즉, DP[i] 는 arr[0]...arr[i]까지 중에서 가장 긴 증가하는 수열의 길이를 의미한다.
현재수가 이전의 수보다 크면 이전의 수의 DP값에서 +1해준다.
현재수보다 작은 이전의 수가 여러개라면 이전의 수의 DP값 중 가장 큰 것을 선택하여 +1해준다.
*/

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define size 1001
#define MAX(a, b) (((a) > (b)) ? (a) : (b))

int main() {
	int N , i, j, max;
	int arr[size];
	int DP[size];

	scanf("%d", &N);
	arr[0] = 0; 
	DP[0] = 0;
	max = 1;

	for (i = 1; i <= N; i++) {
		scanf("%d", &arr[i]);
		DP[i] = 1;
	}

	for (i = 1; i <= N; i++) {
		for (j = 1; j < i; j++) {
			if (arr[i] > arr[j]) {
				DP[i] = MAX(DP[i], DP[j] + 1);
			}

			if (max < DP[i]) {
				max = DP[i];
			}
		}
	}

	printf("%d", max);

	return 0;
}

