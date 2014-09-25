#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int mod(int a, int q) {
    int r = a % q;
    if(r < 0) r += q;
    return r;
}

int gcd(int a, int b) {
    b = abs(b);
    while(b != 0) {
        int r = mod(a, b);
        a = b;
        b = r;
    }
    return a;
}

int process(const int* A, int n) {
    if(n == 1) {
        return A[0];
    }
    if(n == 2) {
        int d = abs(abs(A[0]) - abs(A[1]));
        if(d == 0) {
            return abs(A[0]);
        }
        return d;
    }
    int d = abs(A[0] - A[1]);
    int m = A[0];
    for(int i = 2; i < n; i++) {
        if(m < A[i]) m = A[i];
        d = gcd(d, A[i - 1] - A[i]);
    }
    if(d == 0)
        d = m;

    return d;
}

int main(int argv, const char** args) {
    int A[1000];
    while(true) {
        int n = 0;
        for(n = 0; n < 1000; n++) {
            int a;
            cin >> a;
            if(a == 0) break;
            A[n] = a;
        }
        if(n == 0) break;

        int d = process(A, n);
        cout << d << endl;
    }

    return 0;
}

