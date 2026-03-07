#include <stdio.h>

int main() {
    int n;
    int x = 1;

    printf("Digite um numero inteiro: ");
    scanf("%d", &n);

    for(int i = 1; i <= n; i++) {
        x *= i;
    }
    printf("%d! e: %d", n, x);
}