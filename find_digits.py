for _ in range(input()):
    y = input()
    k = str(y)
    s = []
    for i in range(len(k)):
        if int(k[i]) != 0 :
            if y%(int(k[i])) == 0 :
                s.append(int(k[i]))
    print len(s)        
            
