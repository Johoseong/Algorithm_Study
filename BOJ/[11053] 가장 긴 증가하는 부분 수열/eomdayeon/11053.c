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
