import sys
from datetime import datetime


print 'before import', sys.path,sys.modules.keys()
import import_part2
print '\n\n\n'
print 'after import', sys.path,sys.modules.keys()
