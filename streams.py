def ints(start, end = None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1

def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    yield 0
    for i in ints(1):
        yield +i
        yield -i

j = ints(1)
k = all_ints()
for i in xrange(0,20):
  print next(j), next(k)
