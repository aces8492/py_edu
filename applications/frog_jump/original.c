#include <stdio.h>
#include <stdlib.h>

void print_field(int ,int*);

int main(int argc, char *argv[]) {
	int i, count, loop_flag; 
	int field_size, left_num, light_num;
	int *field;

	if(argc != 4) {
		printf("error : please input 3 nums\n");
		exit(1);
	}

	field_size = atoi(argv[1]);
	left_num = atoi(argv[2]);
	light_num = atoi(argv[3]);

	if(field_size > 14 || field_size < left_num + light_num) {
		printf("error : field size > 14 | field size > num of frogs\n");
		exit(1);
	}

	printf("field size : %d \n left num : %d \n light num : %d \n", field_size, left_num, light_num);

	field = (int *)malloc(field_size * sizeof(int));

	//フィールドの初期化
	//各フィールドの値として0は何もない状態,1は右向きのカエル,2は左向きのカエルとして設定
	for(i = 0; i < field_size; i++) {
		field[i] = 0;
	}
	for(i = 0; i < left_num; i++) {
		field[i] = 1;
	}
	for(i = field_size - 1; i > field_size - 1 - light_num; i--) {
		field[i] = 2;
	}
	printf("target\n");
	print_field(field_size, field);

	printf("intermediate results\n");

	//カエル跳びゲーム
	while(1) {
		for(i = 0; i < field_size; i++) {
			if(field[i] == 0) {
				continue;		
			}
			else if(field[i] == 1) {
				if(i < field_size - 1 && field[i+1] == 0) {
					// |20112|の様な積み状態を回避する
					if(i < field_size - 3 && field[i+2] == 1 && ((i + 3 == field_size - 1 && field[field_size-1] == 2) || (i + 3 > field_size - 1 && i + 4 != 0))) {
						continue;
					}
					field[i] = 0;
					field[i+1] = 1;
					loop_flag++;
					count++;
					print_field(field_size, field);
				}
				else if(i < field_size - 2 && field[i+1] == 2 && field[i+2] == 0) {
					field[i] = 0;
					field[i+2] = 1;
					loop_flag++;
					count++;
					print_field(field_size, field);
				}
			}
			else if(field[i] == 2) {
				if(i > 0 && field[i-1] == 0) {
					if(i > 2 && field[i-2] == 2 && ((i - 3 == 0 && field[0] == 1) || (i -3 > 0 && i - 4 != 0))) {
						continue;
					}
					field[i] = 0;
					field[i-1] = 2;
					loop_flag++;
					count++;
					print_field(field_size, field);
				}
				else if(i > 1 && field[i-1] == 1 && field[i-2] == 0) {
					field[i] = 0;
					field[i-2] = 2;
					loop_flag++;
					count++;
					print_field(field_size, field);
				}
			}
		}
		if(loop_flag == 0) {
			break;
		}
		else {
			loop_flag = 0;
		}
	}
	printf("result\n");
	print_field(field_size, field);
	printf("%d\n",count);

	free(field);
	return 0;
}

//フィールド確認用関数
void print_field(int field_size, int *field) {
	int i;

	for(i = 0; i < field_size; i++) {
		printf("%d ",field[i]);
	}
	printf("\n");
}

