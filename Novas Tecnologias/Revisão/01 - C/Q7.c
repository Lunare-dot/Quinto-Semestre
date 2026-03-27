#include <stdio.h>

int main() {
    double pi = 0.0;
    long n = 1000;
    int sign = 1;

    for(int i = 0; i < n; i++) {
        pi += sign * (1 / (2 * i + 1));
    }
    pi *= 4;

    printf("Aproximacao: %.10f", pi);
    return 0;
}

//Incompleta