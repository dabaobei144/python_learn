def sqrt(n):
    return n*n

#map
a = [1,2,3,-1,-2,-3]
print map(sqrt, a)
print map(lambda x:x**2, [1,2,3,-1,-2,-3])

#filter
a = [1,2,3,4,5,6]
print filter(lambda x:x%2 , a)
print [x for x in a if x%2]

a=[1,2,3]
b=[4,2,3]
c=[5,2,3]
d=[a,b,c]
for item in d:
  for i in item:
    print i
print [i for item in d for i in item]
