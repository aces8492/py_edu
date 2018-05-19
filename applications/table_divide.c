#include<stdio.h>

int main(void) {
	int i, tables, visitors, patterns;

	scanf("%d %d", &tables, &visitors);

	if(tables < 0 || visitors < 0 || tables > 80 || visitors > 80 || tables > visitors) {
	   printf("illegal num\n");	
	   printf("plese input |0 < m < n <= 80|\n");
	}

	patterns = 0;
	for(i = 1; i <= tables; i++) {
		
	}
	
	printf("%d\n",patterns);
	return 0;
}
