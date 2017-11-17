g = 2
print 'g in %s:' %(__file__,), g

def goo():
    global g
    g = 222222
    print 'g in %s.%s:' %(__file__, 'foo'), g, globals()['g']
