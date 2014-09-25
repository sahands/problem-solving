import random


light_switch = False


class Prisoner(object):
    visited = False

    def visit(self):
        self.visited = True
        return False


class RegularPrisoner(Prisoner):
    switched = False

    def visit(self):
        global light_switch
        if light_switch and not self.switched:
            light_switch = False
            self.switched = True

        return super(RegularPrisoner, self).visit()


class ChosenOne(Prisoner):
    count = 0
    prisoner_count = 0

    def __init__(self, prisoner_count):
        self.prisoner_count = prisoner_count

    def visit(self):
        # print "Chosen one visiting - ", self.count
        global light_switch
        if not light_switch:
            light_switch = True
            self.count += 1

        super(ChosenOne, self).visit()
        return self.count == self.prisoner_count


def run_experiment(prisoner_count):
    global light_switch
    light_switch = False
    prisoners = [ChosenOne(prisoner_count)] + \
                [RegularPrisoner() for __ in xrange(prisoner_count - 1)]
    total_visits = 0
    while True:
        # print [r.visited for r in prisoners]
        p = random.choice(prisoners)
        total_visits += 1
        #print prisoners.index(p)
        if p.visit():
            assert False not in [r.visited for r in prisoners]
            #print "Total visits =", total_visits
            break

    return total_visits


def E(m):
    n = e = 1.0
    for __ in xrange(m):
        yield e
        n += 1
        e = n + n * (e + 1) / (n - 1)


def harmonics(m):
    h = n = 1.0
    for __ in xrange(m):
        yield h
        n += 1.0
        h += 1.0 / n


if __name__ == "__main__":
    n = 1000
    for prisoner_count in xrange(1, 3):
        total = 0
        for __ in xrange(n):
            total += run_experiment(prisoner_count)
        print "Average visits with %d prisoners over %d experiments = %f" % \
                (prisoner_count, n, float(total) / n)

    e = E(10)
    h = harmonics(10)
    print [e.next() for __ in xrange(10)]
    print [h.next() for n in xrange(1, 11)]
