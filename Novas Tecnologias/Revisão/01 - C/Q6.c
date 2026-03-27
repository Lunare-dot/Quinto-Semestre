#include <stdio.h>
#include <math.h>

int potenciador(int x, int y) {
    int temp = 1;
    for(int i = 0; i < y; i++) {
        temp *= x;
    }
    return temp;
}

int contarDigitos(int n) {
    int count = 0;
    int temp = n;
    while(temp != 0) {
        temp /= 10;
        count++;
    }
    return count;
}

int eArmstrong(int n) {
    int digitos = contarDigitos(n);
    int digito = n;
    int soma = 0;
    while (digito > 0) {
        int d = digito % 10;
        soma += (int)potenciador(d, digitos);
        digito /= 10;
    }
    return soma == n;
}

int main() {
    int num = 99999;
    int start = 1;

    for(int i = start; i <= num; i++) {
        if(eArmstrong(i)) {
            printf("%d\n", i);
        }
    }
    return 0;
}