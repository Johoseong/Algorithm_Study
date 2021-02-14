#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int N;
	int check = 0, sum = 1;

	scanf("%d", &N);

	while (1) {
		if (N <= sum)
			break;
		check += 1;
		sum += 6 * check;
	}

	printf("%d", check+1);

	return 0;
}
