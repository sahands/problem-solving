#include <stdio.h>

#define N 600

int binarySearch(double* H, double h, int n) {
    int start = 0;
    int end = n - 1;
    int m;
    while(start < end - 1) {
        m = (start + end) / 2;
        if(H[m] <= h) {
            start = m;
        } else{
            end = m;
        }
    }
    return end;
}

int main() {
    double H[N];
    int i;
    double h;
    int index;

    H[0] = 0.0;
    for(i = 1; i < N; i++ ) {
        H[i] = H[i-1] + 1.0 / (i + 1);
    }

    while(1) {
        scanf("%lf", &h);
        if(h < 0.001) {
            break;
        }
        index = binarySearch(H, h, N);
        printf("%d card(s)\n", index);
    }
    return 0;
}
