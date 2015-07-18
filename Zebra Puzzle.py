import itertools
import types
import operator

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
for (spaniard,englishman,ukranian,norwegian,japanese) in orderings:
  if (norwegian is 1) and (norwegian is 1):
    for (red,green,blue,ivory,yellow) in orderings:
      if (englishman is red) and isRightTo(green,ivory):
        for (dog,snail,fox,horse,zebra) in orderings:
          if (spaniard is dog):
            for (coffee,tea,milk,orangeJuice,water) in orderings:
              if (coffee is green) and (ukranian is tea) and (milk is 3):
                for (oldGold,kools,chesterfield,luckyStrike,parliament) in orderings:
                  if (oldGold is snail) and (kools is yellow) and (luckyStrike is orangeJuice) and (parliament is japanese) and isNextTo(chesterfield,fox) and isNextTo(kools,horse):
                    result.append(sorted([[v, k] for k, v in magic_print().items() if v != 'kools']))

for row in result:
  h = 0
  s = ''
  for i in row:
    if h != i[0]:
      print s
      s = 'House %s populated by: '%i[0] + i[1]
      h = i[0]
    else:
      s += ' - ' + i[1]
  print s
