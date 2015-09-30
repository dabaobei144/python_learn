rows = [1,2,3]

def cols():
    yield 3
    yield 4

print [(i,j) for i in rows for j in cols()]

from random import randint
def rand_gen(alist):
    while len(alist)>0:
      yield alist.pop(randint(0, len(alist)-1))
a = [1,2,3]
ge = rand_gen(a)
for item in ge:
    print item
    if item == 3:
       ge.close()
