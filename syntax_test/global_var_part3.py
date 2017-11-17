
def goo():
    global g

#    print 'g in %s.%s:' %(__file__, 'foo'), g  # error, global name 'g' is not defined
    g = 333333
    print 'g in %s.%s:' %(__file__, 'foo'), g, globals()['g']
