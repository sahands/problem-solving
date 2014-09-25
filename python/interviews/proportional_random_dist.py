# http://www.geeksforgeeks.org/random-number-generator-in-arbitrary-probability-distribution-fashion/
# Given n numbers, each with some frequency of occurrence, 
# return a random number with probability proportional to 
# its frequency of occurrence.

import random;
import collections;

# My solution is based on the following:
# Let s be the sum of the frequencies and generate a random number
# between 1 and s. Then find out which interval the number falls into.
# Use the interval to pick the number.
# Complexity: O(N) to calculate the sum and O(N) to find the interval. So O(N) total.
def biased_choice(numbers, freqs):
    r = random.randint(1,sum(freqs));
    i = 0; 
    a = 0; # accumulative sum
    while a < r:
        a+=freqs[i];
        i+=1;
    
    return numbers[i-1]
    

if __name__=="__main__":
    n = [1,2,3,4,5];
    d = [1,2,2,1,4];
    counts = collections.defaultdict(int);
    
    for i in range(10000):
        c = biased_choice(n,d);
        counts[c] += 1;
        
    print counts;