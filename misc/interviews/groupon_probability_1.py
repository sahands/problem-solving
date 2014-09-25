import random
import time
import unittest


def bernoulli_process(p):
    if p > 1.0 or p < 0.0:
        raise ValueError("p should be between 0.0 and 1.0.")
    while True:
        yield random.random() > p


def pick_random_coin_from_bag(fair_coin_probablity):
    if random.random() < fair_coin_probablity:
        return bernoulli_process(0.5)
    else:
        return bernoulli_process(1.0)

a = 0  # number of times we get 10 heads in a row AND coin was unfair
b = 0  # total number of times we get 10 heads in a row
for __ in xrange(100000):
    coin = pick_random_coin_from_bag(0.99)
    if True not in [coin.next() for __ in xrange(10)]:
        b += 1
        if coin.gi_frame.f_locals['p'] > 0.6:
            a += 1

print float(a) / b

exit()

def von_neumann_extractor(process):
    while True:
        x, y = process.next(), process.next()
        if x != y:
            yield x


b = bernoulli_process(0.1)
e = von_neumann_extractor(b)
c = 0
for i in xrange(1000):
    f = e.next()
    if f:
        c += 1

print c


exit()


def flip_simple(unfair_coin):
    """Returns Return True (T) or False (F)  with .5 probability, using a (possibly) unfair
    coin flip function.  
    
    The algorithm looks for patterns of the form TF or FT and returns T or F
    depending on which one is reached first.
    
    Assumes unfairCoin is function that returns True with fixed probability p and False
    with fixed probability 1.0-p, , with 0<p<1. An infinite loop is possible if this
    assumption is not met. 
    
    """
    flips = 0
    while True:
        (f1, f2) = (unfair_coin(), unfair_coin())
        flips += 2
        if (f1, f2) == (True, False) or (f1, f2) == (False, True):
            return flips, f1

def fair_coin(unfair_coin):
    """Return True (T) or False (F) with .5 probability, using a (possibly) unfair 
    coin flip function. 
    
    The algorithm looks for patterns of the form T^kF^k or F^kT^k and returns T or F
    depending on which one is reached first. If the pattern is interrupted, the state 
    is reset.
    
    Assumes unfairCoin is function that returns True with fixed probability p and False
    with fixed probability 1.0-p, with 0<p<1.An infinite loop is possible if this
    assumption is not met.
    
    """
    c = dict()  # Used to keep counts of heads and tails so far.
    c[True] = c[False] = 0
    flips = 0
    while True:
        f = unfair_coin()
        flips += 1
        c[f] += 1
        
        if c[True] == c[False]:
            return flips, f
        
        for v in [True,False]:
            if c[v] % 2 == 0 :
                c[v]
        # If the count of tails following heads exceeds the count of heads,
        # the pattern is interrupted. Reset the state. Also vice versa.
        for (f1, f2) in [(True, False), (False, True)]:
            if (c[f1] > c[f2] > 0 and f == f1): 
                c[True] = c[False] = 0



class TestFairCoinTossUsingUnfairCoin(unittest.TestCase):
    
    def setUp(self):
        self.p = 0.3;
        self.startTime = time.time()
        self.unfairCoin = lambda: random.random() < self.p;
        
    def tearDown(self):
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)
        
    def do_test(self,coin):
        headsCount = 0
        total_flips = 0;
        for i in range(10000):
            c, flip = coin(self.unfairCoin)
            total_flips += c
            if flip:
                headsCount += 1
        print "Function:", coin.__name__ 
        print "Heads count:", headsCount
        print "Average number of flips:", total_flips/10000.0

    def test_flipper_simple(self):
        self.do_test(flip_simple)
        print "Calculated expected number of flips:", 1.0/(self.p*(1.0-self.p))
        
    def test_flipper_complete(self):
        self.do_test(fair_coin)
        

if __name__ == '__main__':
    #unittest.main()
    pass;