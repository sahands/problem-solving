from __future__ import division
from math import sqrt, atan2, pi
from sys import stdin

__author__ = "Sahand Saba"


EPS = 1e-6


class Point(object):
    __slots__ = ['x', 'y']

    def __init__(self, xx=0.0, yy=0.0):
        self.x = float(xx)
        self.y = float(yy)

    def angle(self):
        """
        Returns the angle the point makes with the x-axis,
        counter-clockwise. Result is in the [0, 2*pi) range.
        """
        a = atan2(self.y, self.x)
        if a < 0:
            a = 2 * pi + a
        return a


class Circle(object):
    __slots__ = ['center', 'radius']

    def __init__(self, center, radius):
        self.center = center
        self.radius = float(radius)

    def common_tangents(self, other):
        """
        Returns [[p1,p2],[q1,q2]] with p1, p2, q1, q2 all Point objects
        representing points on C1 such that the tangent lines to C1 at p1, p2,
        q1, q2 are tangent to C2 as well. Further more, p1 and p2 represent
        external tangent lines, while q1 and q2 represent internal ones. It is
        also guaranteed that p1 and q1 are both on the left-side of the line
        connecting C1.center to C2.center, and p2 and q2 are on the right-side
        of it.
        """
        C1, C2 = self, other
        mu = C1.center.x - C2.center.x
        eta = C1.center.y - C2.center.y
        r1 = C1.radius
        r2 = C2.radius
        r1r1 = r1 * r1
        r1r2 = r1 * r2
        delta1 = r1r1 - r1r2
        delta2 = r1r1 + r1r2
        mumu = mu * mu
        etaeta = eta * eta
        D = etaeta + mumu
        result = [[], []]
        if abs(D) < EPS:
            return result

        if abs(eta) < EPS:
            # In this case there is symmetry along the x-axis and we can
            # not divide by eta. Use x^2 + y^2 = r^2 to find y.
            dmu = -1 if mu < 0 else 1
            x = (-delta1 * mu) / D
            y = -dmu * sqrt(r1r1 - x * x)
            result[0].append(Point(x, y))
            result[0].append(Point(x, -y))
            x = (-delta2 * mu) / D
            y = -dmu * sqrt(r1r1 - x * x)
            result[1].append(Point(x, y))
            result[1].append(Point(x, -y))
        else:
            # Here, the symmetry is along the line connecting the two centers.
            # Use the equation eta*y + mu *x + r1^2 - r1 * r2 = 0 to derive y
            # since we can divide by eta.
            dd1 = delta1 * delta1
            dd2 = delta2 * delta2
            Delta1 = sqrt(dd1 * mumu - D*(dd1 - etaeta * r1r1))
            Delta2 = sqrt(dd2 * mumu - D*(dd2 - etaeta * r1r1))
            deta = -1 if eta < 0 else 1
            x = (-delta1 * mu + deta * Delta1) / D
            result[0].append(Point(x, -(mu*x + delta1)/eta))
            x = (-delta1 * mu - deta * Delta1) / D
            result[0].append(Point(x, -(mu*x + delta1)/eta))
            x = (-delta2 * mu + deta * Delta2) / D
            result[1].append(Point(x, -(mu*x + delta2)/eta))
            x = (-delta2 * mu - deta * Delta2) / D
            result[1].append(Point(x, -(mu*x + delta2)/eta))

        return result


def add_events(A, p, q):
    start = p.angle()
    end = q.angle()
    A.append((start, 1, p))
    A.append((end, -1, q))
    return 1 if start > end else 0


def max_intersecting_line(C):
    """
    Given a list of circles, returns (m, c, p) where m is the maximal number of
    circles in C any line can intersect, and p is a point on a circle c in C
    such that the tangent line to c at p intersects m circles in C.
    """
    global_max = 1
    solution_circle = C[0]
    solution_point = Point(C[0].radius, 0.0)
    for c1 in C:
        local_max = 1
        A = []

        for c2 in (c for c in C if c is not c1):
            Q = c1.common_tangents(c2)
            t1 = add_events(A, Q[1][0], Q[0][0])
            t2 = add_events(A, Q[0][1], Q[1][1])
            local_max += max(t1, t2)

        if local_max > global_max:
            global_max = local_max
            solution_point = Point(c1.radius, 0.0)
            solution_circle = c1

        A.sort()
        for a in A:
            local_max += a[1]
            if local_max > global_max:
                global_max = local_max
                solution_point = Point(c1.center.x + a[2].x,
                                       c1.center.y + a[2].y)
                solution_circle = c1
    return global_max, solution_circle, solution_point


if __name__ == '__main__':
    T = int(stdin.readline())
    for __ in xrange(T):
        n = int(stdin.readline())
        C = []
        for i in xrange(n):
            x, y, r = tuple(stdin.readline().split(' '))
            C.append(Circle(Point(x, y), r))
        print max_intersecting_line(C)[0]
