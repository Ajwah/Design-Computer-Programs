import itertools
import types
import operator
import time

def timedCall(fn, *args):
  'Call function and report elapsed time'
  t0 = time.clock()
  r = fn(*args)
  t1 = time.clock()
  return t1-t0, r

def timedCalls(n,fn,*args):
  def average(nums):
    return sum(nums)/float(len(nums))

  'Repeatedly call function n amount of times if n is int else for n seconds if n is float'
  if isinstance(n,int):
    times = [timedCall(fn,*args)[0] for _ in range(n)]
  else:
    times = []
    while sum(times)<n:
      times.append(timedCall(fn,*args)[0])
  return min(times), average(times), max(times), sum(times)


def zebra_puzzle():
  'Solve Zebra Puzzle completely and return solution for output'
  #List of local variables to be excluded from listing
  exclude = ['orderings','houses','result','exclude','x', 'l', 'k', 'v']

  def isNextTo(h,to):
    return isRightTo(h,to) or isRightTo(to,h)

  def isRightTo(h,to):
    return h == to + 1

  houses = range(1,6)
  orderings = list(itertools.permutations(houses))
  result = []

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
                      #Obtain all local variables with their corresponding values
                      l = locals().iteritems()
                      #Extract from l those that are relevant to the puzzle
                      x = sorted([(k,v) for k,v in l if (k not in exclude and
                                                        type(v) is not types.FunctionType and
                                                        type(v) is not types.StringType)])
                      #Include the line as a valid and possible solution
                      result.append(sorted([[v, k] for k, v in x]))
  return result

def output():
  n = 1000
  t, result = timedCall(zebra_puzzle)
  minT, avT, maxT, totT = timedCalls(n, zebra_puzzle)
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
  print 'Time to execute entire function: ', t
  print 'Minimum Time to execute function %s times: '%n, minT
  print 'Average Time to execute function %s times: '%n, avT
  print 'Maximum Time to execute function %s times: '%n, maxT
  print 'Total Time to execute function %s times: '%n, totT


output()
