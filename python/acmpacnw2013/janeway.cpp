#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

double EPS = 1e-6;

class Point {
    public:
        double x, y;
        Point(double x=0.0, double y=0.0) : x(x), y(y) {}
        double angle() const {
            double a = atan2(y, x);
            if (a < 0) {
                a = atan(1) * 8.0 + a;
            }
            return a;
        }
};

class Event {
    public:
        double angle;
        double count;
        Event(double angle = 0, int count = 1) : angle(angle), count(count) {}
        bool operator<(const Event &o) const {
            return angle < o.angle;
        }
};

struct CircleCircleTangents {
    public:
        Point external[2];
        Point internal[2];
};

class Circle {
    public:
        Point center;
        double radius;
        Circle(double x=0.0, double y=0.0, double r=1.0) : radius(r), center(x,y) {}

        // external[0] and internal[0] are guaranteed to be on the left-side of
        // the directed line contennting C1.center to C2.center
        CircleCircleTangents commonTangents(const Circle& C2) const {
            const Circle& C1 = *this;
            double mu = C1.center.x - C2.center.x;
            double eta = C1.center.y - C2.center.y;
            double r1 = C1.radius;
            double r2 = C2.radius;
            double r1r1 = r1 * r1;
            double r1r2 = r1 * r2;
            double delta1 = r1r1 - r1r2;
            double delta2 = r1r1 + r1r2;
            double D = eta*eta + mu*mu;
            CircleCircleTangents result;
            if (abs(eta) < EPS){
                // Do not divide by eta! Use x^2 + y^2 = r^2 to find y.
                double dmu = mu < 0? -1 : 1;
                double x = (-delta1 * mu) / D;
                double y = -dmu * sqrt(r1r1 - x * x);
                result.external[0].x = x;
                result.external[0].y = y;
                result.external[1].x = x;
                result.external[1].y = -y;
                x = (-delta2 * mu) / D;
                y = -dmu * sqrt(r1r1 - x * x);
                result.internal[0].x = x;
                result.internal[0].y = y;
                result.internal[1].x = x;
                result.internal[1].y = -y;
            } else {
                // Dividing by eta is ok. Use mu*x + eta*y + delta = 0 to find y.
                double mumu = mu * mu;
                double etaeta = eta * eta;
                double dd1 = delta1 * delta1;
                double dd2 = delta2 * delta2;
                double deta = eta < 0? -1 : 1;
                double Delta1 = deta * sqrt(dd1 * mumu - D*(dd1 - etaeta * r1r1));
                double Delta2 = deta * sqrt(dd2 * mumu - D*(dd2 - etaeta * r1r1));
                double x = (-delta1 * mu + Delta1) / D;
                result.external[0].x = x;
                result.external[0].y = -(mu*x + delta1)/eta;
                x = (-delta1 * mu - Delta1) / D;
                result.external[1].x = x;
                result.external[1].y = -(mu*x + delta1)/eta;
                x = (-delta2 * mu + Delta2) / D;
                result.internal[0].x = x;
                result.internal[0].y = -(mu*x + delta2)/eta;
                x = (-delta2 * mu - Delta2) / D;
                result.internal[1].x = x;
                result.internal[1].y = -(mu*x + delta2)/eta;
            }
            return result;
        }
};

bool add_events(vector<Event>& A, const Point& p, const Point& q) {
    double start = p.angle();
    double end = q.angle();
    A.push_back(Event(start, 1));
    A.push_back(Event(end, -1));
    return start > end;
}

// Given a list of circles, returns (m, c, p) where m is the maximal number of
// circles in C any line can intersect, and p is a point on a circle c in C
// such that the tangent line to c at p intersects m circles in C.
int max_intersecting_line(const Circle* C, int n) {
    int global_max = 1;
    vector<Event> A;
    for(int i = 0; i < n; i++) {
        const Circle& c1 = C[i];
        A.clear();
        int local_max = 1;
        for(int j = 0; j < n; j++) {
            if(j == i) continue;
            const Circle& c2 = C[j];
            CircleCircleTangents Q = c1.commonTangents(c2);
            bool t1 = add_events(A, Q.internal[0], Q.external[0]);
            bool t2 = add_events(A, Q.external[1], Q.internal[1]);
            if(t1 || t2) {
                local_max++;
            }
        }

        if (local_max > global_max) {
            global_max = local_max;
        }

        sort(A.begin(), A.end());
        for(int i = 0; i < A.size(); i++) {
            local_max += A[i].count;
            if(local_max > global_max) {
                global_max = local_max;
            }
        }
    }
    return global_max;
}

int main() {
    Circle C[2000];
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n;
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> C[i].center.x >> C[i].center.y >> C[i].radius;
        }

        cout << max_intersecting_line(C, n) << endl;
    }
    return 0;
}
