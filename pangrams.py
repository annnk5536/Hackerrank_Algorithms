def pangram(s):
     return set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())
s = raw_input()
if pangram(s)== set([]) :
    print 'pangram'
else:
    print 'not pangram'
