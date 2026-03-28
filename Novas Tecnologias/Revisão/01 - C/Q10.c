#include <stdio.h>

int fibo(int pos) {
    if(pos<= 2) return  1;
    else return fibo(pos - 1) + fibo(pos - 2);
}

int main() {
    //1, 1, 2, 3, 5, 8, 13, 21...
    int pos, ant, post, aux;

    printf("Entre com a pos: ");
    scanf("%d", &pos);

    ant = 1;
    post = 1;

    /*
    for(int i = 2; pos > i; i++) {
        aux = post;
        post = ant + post;
        ant = aux;
    }*/

    printf("Fibo(%d) = %d", pos, fibo(pos));
}