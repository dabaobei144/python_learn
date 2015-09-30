numbers = set();
while (True):
  number = raw_input("please input a number which is not inputed before:\n")
  if False == number.isdigit():
    print 'input is not number'
    continue
  number = int(number)
  if number== -1:
    print 'nijia'
    break
  if number in numbers:
    print str(number) + ' already exists!'
  else:
    numbers.add(number)
    print 'succeed!'
  print '\n'
