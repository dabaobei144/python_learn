#None
print None
print None is None
print None == None

#int
a = 10
print a

#srting
a = 'hello'
print a

#double
a = 11.111
print a

#bool
a = True
print a

#list
a = [1,2,3]
print a
print len(a)
a.append(4)
print a, a.index(1), a.pop()
print a[0], a[-1]
for item in a:
  print item

#tuple
a = ('nijia', 2, True, None)
print a
for item in a:
  print item

#set
a = set([1,2,2,3,4])
print a
for item in a:
  print item

#dict
a = {'name':'nijia', 'age':10}
print a
for key,value in a.items():
  print key, value
for key in a.keys():
  print key
for value in a.values():
  print value
a = dict(name='nijia', age=10)
a['name'] = 'nijia2'
print a, a.has_key('name'), a.has_key('sex'), a['name'], a.pop('age')
del a['name']
print a
