#include <stdio.h>

int isPrime(int num) {
    if (num <= 1) return 0;
    if (num <= 3) return 1;
    if (num % 2 == 0 || num % 3 == 0) return 0;

    int i = 5;
    while (i * i <= num) {
        if (num % i == 0 || num % (i + 2) == 0) return 0;
        i += 6;
    }
    return 1;
}

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 2; i <= n; i++) {
        if (isPrime(i)) {
            printf("%d ", i);
        }
    }

    return 0;
}



// run gcc prime.c -o prime
// then run ./prime