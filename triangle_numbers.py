n = input()
for _ in range(n):
    k = input()
    if k<=2 :
        print -1
    elif k%2 != 0:
        print 2
    elif k%4 == 0 :
        print 3
    else:
        print 4
