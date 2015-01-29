import sys
if __name__ == '__main__':
    l = int(sys.stdin.readline())
    r = int(sys.stdin.readline())
    print (max(a ^ b for a in range(l,r+1) for b in range(l,r+1)))
