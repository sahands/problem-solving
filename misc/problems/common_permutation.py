from collections import Counter

def common_permutation(a, b):
    return ''.join(k * v for k, v in sorted((Counter(a) & Counter(b)).items()))

print common_permutation('pretty', 'women')
print common_permutation('walking', 'down')
print common_permutation('the', 'street')
print common_permutation('aaabbbbccdddddd', 'bbdddcccaaaaaaadd')
print common_permutation('bbdddcccaaaaaaadd','aaabbbbccdddddd')
