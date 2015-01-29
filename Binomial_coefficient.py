for _ in range(input()):
        n, P = [int(x) for x in raw_input().split()]
        m = n
        k = 1
        while m > 0:
            k *= (m % P) + 1
            m //= P
        
        print n + 1 - k
