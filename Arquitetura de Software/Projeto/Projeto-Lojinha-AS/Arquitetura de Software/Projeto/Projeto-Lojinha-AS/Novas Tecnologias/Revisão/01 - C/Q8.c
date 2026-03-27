#include <stdio.h>
#include <math.h>
#define pi 3.14

int fatorial(int num) {
    int fat = 1;
    while(num > 0) {
        fat = fat * num;
        num--;
    }
}

int main() {
    float grau, rad, cos = 0, sinal = 1;

    printf("Qual o valor do grau? ");
    scanf("%f", &grau);

    rad = pi*grau/180;

    for(int i = 0; i <=10; i+= 2) {
        cos = cos + sinal * pow(rad, i)/fatorial(i);
        sinal = sinal * (-1);
    }

    printf("cos(%.2f) = %f", grau, cos);
}