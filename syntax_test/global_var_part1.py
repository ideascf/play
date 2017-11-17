g = 1
print 'before import global_var_part2, g in %s:' %(__file__,), g
import global_var_part2
print 'after import global_var_part2, g in %s:' %(__file__,), g
import global_var_part3
print 'after import global_var_part3, g in %s:' %(__file__,), g

def foo():
    global g
    print 'g in %s.%s:' %(__file__, 'foo'), g

global_var_part2.goo()
print 'after global_var_part2.goo(), g in %s:' %(__file__,), g, globals()['g']

global_var_part3.goo()
print 'after global_var_part3.goo(), g in %s:' %(__file__,), g, globals()['g']

foo()
print 'after global_var_part1.foo(), g in %s:' %(__file__,), g, globals()['g']
