#define _CRT_SECURE_NO_WARNINGS_
#include <stdio.h>

int dp[10001], n, k, value[101];

int main()
{
	scanf("%d %d", &n, &k);
	for (int i = 1; i <= n; i++)
		scanf("%d", &value[i]);

	dp[0] = 1;
	for (int i = 1; i <= n; i++) {
		for (int j = value[i]; j <= k; j++) {
			dp[j] += dp[j - value[i]];
		}
	}

	printf("%d\n", dp[k]);

	return 0;
}