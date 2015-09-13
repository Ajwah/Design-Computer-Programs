import itertools
import types
import operator

# Everything after this counts
d = dict(globals())
result = []
def kv_test(k,v):
    return (k not in d and
            k not in ['d','args'] and
            type(v) is not types.FunctionType and
            k != 'orderings' and k != 'houses' and k!= 'result' and k != 'i' and k != 'row' and k != 's')

def magic_print(*args):
    if len(args) == 0:
        return {k:v for k,v in globals().iteritems() if kv_test(k,v)}
    else:
        return {k:v for k,v in magic_print().iteritems() if k in args}

houses = range(1,6)
orderings = list(itertools.permutations(houses))

def isNextTo(h,to):
  return isRightTo(h,to) or isRightTo(to,h)

def isRightTo(h,to):
  return h == to + 1
def isLeftTo(h,to):
  return h == to - 1

for (brittish, swedish, danish, norwegian, german) in orderings:
  if (norwegian is 1):
    for (red,green,blue,white,yellow) in orderings:
      if (brittish is red) and isLeftTo(green,white):
        for (dog, birds, cats, horse, fish) in orderings:
          if (swedish is dog):
            for (tea, coffee, milk, beer, water) in orderings:
              if (coffee is green) and (danish is tea) and (milk is 3):
                for (PallMall, Dunhill, Blends, Bluemasters, Prince) in orderings:
                  if (PallMall is birds) and (Dunhill is yellow) and (Bluemasters is beer) and (Prince is german) and isNextTo(norwegian,blue) and isNextTo(Blends,water) and isNextTo(Blends, cats):
                    result.append(sorted([[v, k] for k, v in magic_print().items() if v != 'kools']))

for row in result:
  h = 0
  s = ''
  print h, row
  for i in row:
    # print i[0], i[1], h
    if h != i[0]:
      print s
      s = 'House %s populated by: '%i[0] + i[1]
      h = i[0]
    else:
      s += ' - ' + i[1]
  print s

  House   #1        #2     #3    #4      #5
  Color   Yellow    Blue   Red   Green   White
  Natl    Norweg    Dane   Brit  German  Swede
  Bevg    Water     Tea    Milk  Coffee  Beer
  Smokes  Dunhill   Blends PallM Prince  BlueM
  Pet     Cat       Horse  Birds Fish    Dogs
