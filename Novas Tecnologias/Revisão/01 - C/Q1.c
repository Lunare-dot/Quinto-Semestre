#include <stdio.h>

int validador(int *temp);

int main() {
    int num;
    int i = 0;
    int x[5];

    printf("Insira um numero de cinco digitos: ");
    scanf("%d", &num);

    if(validador(&num) == 1) {
        return 1;
    } else {
        while(num > 0) {
            x[i] = num % 10;
            num /= 10;
            i++;
        }
    }

    printf("%d %d %d %d %d", x[4], x[3], x[2], x[1], x[0]);
}

int validador(int *temp) {
    int count = 0;
    int copia = *temp;

    while (copia > 0) {
        copia /= 10;
        count++;
    }

    if (count != 5) {
        printf("O numero deve conter cinco digitos.");
        return 1;
    }

    return 0;
}