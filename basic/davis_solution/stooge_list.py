#!/usr/bin/python -tt
list = ['larry', 'curly', 'moe']
print "code: list = ['larry', 'curly', 'moe']"
print list
print '----------------------------------------------------'

list.append('shemp')				## append elem at end
print "code: list.append('shemp')"		## append elem at end
print list
print '----------------------------------------------------'

list.insert(0, 'xxx')				## insert elem at index 0
print "code: list.insert(0, 'xxx')"		## insert elem at index 0
print list
print '----------------------------------------------------'

list.extend(['yyy', 'zzz'])			## add list of elems at end
print "code: list.extend(['yyy', 'zzz'])"	## add list of elems at end
print list
print '----------------------------------------------------'

print "code: print list.index('curly')"
print list.index('curly')
print '----------------------------------------------------'

list.remove('curly')
print "code: list.remove('curly')"
print list
print '----------------------------------------------------'

list.pop(1)
print "code: list.pop(1)"
print list
print '----------------------------------------------------'

list.pop()
print "code: list.pop()"
print list
