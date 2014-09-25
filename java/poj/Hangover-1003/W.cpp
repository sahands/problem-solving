#include <stdio.h>
#include <iostream>

using namespace std;

int binarySearch(const double* H, const double h, const int n) {
    int start = 0;
    int end = n - 1;
    while(start < end - 1) {
        int m = (start + end) / 2;
        if(H[m] <= h) {
            start = m;
        } else{
            end = m;
        }
    }
    return end;
}

int main() {
    const int N = 600;
    double H[N];
    H[0] = 0.0;
    for(int i = 1; i < N; i++ ) {
        H[i] = H[i-1] + 1.0 / (i + 1);
    }

    while(true) {
        double h;
        cin >> h;
        if(h < 0.001) {
            break;
        }
        int index = binarySearch(H, h, N);
        printf("%d card(s)\n", index);
    }
}
