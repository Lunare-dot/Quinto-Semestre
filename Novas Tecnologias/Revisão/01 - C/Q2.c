#include <stdio.h>
#include <math.h>

int main() {
    float num = 5;
    float x;

    for(int i = 1; i < (num * 2); i++) {
        if((i % 2) == 1) {
            x += i;
        }
    }

    printf("%.f\n", pow(num, 2));

    if(fabs(x - pow(num, 2)) < 1e-6) {
        printf("O quadrado de %.f e: %.f", num, x);
    } else {
        printf("ERROR");
    }

}