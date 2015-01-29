import sys
if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for _ in range(t):
        n,k = list(map(int, sys.stdin.readline().split()))

        if n <= 4 * k:
            print(n - 1)
        else:
            d = n * n - 4 * n * k
            minRoot = (n - d**0.5) / 2
            maxRoot = (n + d**0.5) / 2
            
            print(int(minRoot) + int(n - maxRoot))
