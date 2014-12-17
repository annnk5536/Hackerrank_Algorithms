n = input()
import math
def c(x,y): return math.factorial(x)/(math.factorial(y)*math.factorial(x-y))
for _ in range(n):
    n = input()
    k = input()
    print int(c(n+k-1,k) % 1000000000)
