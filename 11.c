#include <stdio.h>

int main() {
    int a, b;
    printf("请输入两个整数：");
    scanf("%d %d", &a, &b);

    printf("加法结果：%d\n", a + b);
    printf("减法结果：%d\n", a - b);

    return 0;
}