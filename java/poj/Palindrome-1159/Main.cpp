#include <iostream>

using namespace std;

const int N = 5000;

int M0[N];
int M1[N];
int M2[N];

int palindrome(const char* c, int n) {
    for(int j = 0; j < n; j++) {
        M0[j] = 0;
    }

    for(int k = 1; k <= n; k++) {
        for(int i = n - 1 - k; i >= 0; i--) {
            if(c[i] == c[i + k]) {
                M2[i] = M0[i + 1];
            } else {
                int t1 = M1[i];
                int t2 = M1[i + 1];
                int t = t1 < t2 ? t1: t2;
                M2[i] = t + 1;
            }
        }
        for(int j = 0; j < n; j++) {
            M0[j] = M1[j];
            M1[j] = M2[j];
        }
    }
    return M2[0];
}

int main() {
    char c[N];
    int n;
    cin >> n >> c;
    cout << palindrome(c, n) << endl;
    return 0;
}
