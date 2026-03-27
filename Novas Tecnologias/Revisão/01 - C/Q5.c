#include <stdio.h>
#include <math.h>

int main() {
    int n;
    int x = 0;

    printf("Digite um numero inteiro: ");
    scanf("%d", &n);

    for(int i = 1; i < (n * 2); i++) {
        if((i % 2) == 1) {
             x += i;
        }
    }

    int y = pow(n, 2);
    printf("%d\n", y);

    if(x == pow(n, 2)) {
        printf("O quadrado de %d e %d", n, x);
    } else {
        printf("ERROR!");
    }
}