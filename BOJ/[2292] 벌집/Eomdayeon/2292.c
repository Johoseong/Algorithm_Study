#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define MAX 1000000000

int main() {
	int N; //숫자 N번방
	int j = 1;  
	int count = 1;	//지나가는 최소의 방 개수 count

	scanf("%d", &N);
	
	while (N<1 || N>MAX) {
		scanf("%d", &N);
	}

	while (N > j) {
		j = j + 6 * count;
		count++;
	}
	printf("%d", count) ;

	return 0;
}
