def sum_of_multiples(k, n):
    """Returns the sum of all multiples of k less than n."""
    m = (n-1) // k
    return k * (m * (m + 1)) / 2

if __name__ == '__main__':
    n = 1000
    a = sum_of_multiples(3, n)
    b = sum_of_multiples(5, n)
    c = sum_of_multiples(15, n)

    print a + b - c


