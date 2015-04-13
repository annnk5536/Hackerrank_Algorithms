for _ in xrange(input()): #using xrange as generator instead of range works with more efficiency
        n, P = [int(x) for x in raw_input().split()]
        m = n
        k = 1
        while m > 0:
            k *= (m % P) + 1
            m //= P
        
        print n + 1 - k
