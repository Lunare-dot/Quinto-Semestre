#include <stdio.h>

int main() {
    int I;
    float x[] = {10, 1, 7};
    float n = sizeof(x) / sizeof(x[0]);

    printf("Digite um numero inteiro de 1 a 3: ");
    scanf("%d", &I);

    switch(I) {
        case 1:
            for(int i = 0; i < n - 1; i++) {
                for(int j = 0; j < n - i - 1; j++) {
                    if(x[j] > x[j + 1]) {
                        float temp = x[j];
                        x[j] = x[j + 1];
                        x[j + 1] = temp;
                    }
                }
            }
            for(int i = 0; i < n; i++) {
                printf("%.f ", x[i]);
            } break;

        case 2:
            for(int i = 0; i < n - 1; i++) {
                for(int j = 0; j < n - i - 1; j++) {
                    if(x[j] < x[j + 1]) {
                        float temp = x[j];
                        x[j] = x[j + 1];
                        x[j + 1] = temp;
                    }
                }
            }
            for(int i = 0; i < n; i++) {
                printf("%.f ", x[i]);
            } break;

        case 3: {
            int max = 0;
            for(int i = 1; i < n; i++) {
                if(x[i] > x[max]) max = i;
            }

            float o[2];
            int k = 0;
            for(int i = 0; i < n; i++){
                if(i != max) {
                    o[k++] = x[i];
                }
            }

            printf("%.f %.f %.f", o[0], x[max], o[1]);
            break;
        }    

        default:
            if(I > 3 || I < 3) printf("Insira um número válido de 1 a 3.");
            break;
    }
}

/*Bubble Sort em ordem crescente: Se o elemento atual for maior que o próximo, o algoritmo irá:
Passar o valor do elemento atual para uma variável auxiliar (temp = x[j]),
em sequência irá passar o valor do próximo elemento (x[j + 1]) para o atual (x[j]) e, por fim,
irá passar o valor temporário para o x[j + 1], repetindo até que a ordenação esteja completa*/