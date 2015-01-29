def dotp(a,b):
    assert len(a) == len(b), 'vector'
    return sum(aterm * bterm for aterm,bterm in zip(a, b))
def crossProd(a,b):
      dimension = len(a)
      c = []
      for i in range(dimension):
        c.append(0)
        for j in range(dimension):
          if j != i:
            for k in range(dimension):
              if k != i:
                if k > j:
                  c[i] += a[j]*b[k]
                elif k < j:
                  c[i] -= a[j]*b[k]
      return c
n = input()
for i in range(n):
    s1 = raw_input().split()
    s2 = raw_input().split()
    s3 = raw_input().split()
    s4 = raw_input().split()
    v1 = [int(x) for x in s1]
    v2 = [int(x) for x in s2]
    v3 = [int(x) for x in s3]
    v4 = [int(x) for x in s4]
    vector_1 = [v1[0]-v2[0],v1[1]-v2[1],v1[2]-v2[2]]
    vector_2 = [v2[0]-v3[0],v2[1]-v3[1],v2[2]-v3[2]]
    vector_3 = [v3[0]-v4[0],v3[1]-v4[1],v3[2]-v4[2]]
    if dotp(crossProd(vector_1,vector_2),vector_3) == 0:
        print  'YES'
    else:
         print  'NO'
    
