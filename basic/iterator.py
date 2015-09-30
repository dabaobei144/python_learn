#list
names = ['nijia', 'shengdongjie', 'zhoubin']
iter = iter(names)
#print iter.next()
#print iter.next()
#print iter.next()
#print iter.next()

#iter = iter(names)
while True:
    try:
      name = iter.next()
    except StopIteration:
        print 'iteration stop!'
        break
    print name
