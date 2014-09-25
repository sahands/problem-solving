#include <iostream>

using namespace std;


double solve(double C, double F, double X) {
    double r = 2.0;
    double t = 0.0;
    while(true) {
        if(C + (r * X) / (r + F) < X) {
            t += C / r;
            r += F;
        }
        else {
            return t + X / r;
        }
    }
}

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        double C, F, X;
        cin >> C >> F >> X;
        cout << "Case #" << t << ": " << solve(C, F, X) << endl;
    }
}
