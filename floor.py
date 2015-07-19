#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on
# different floors of a five-floor apartment building.
#
# Hopper does not live on the top floor.
# Kay does not live on the bottom floor.
# Liskov does not live on either the top or the bottom floor.
# Perlis lives on a higher floor than does Kay.
# Ritchie does not live on a floor adjacent to Liskov's.
# Liskov does not live on a floor adjacent to Kay's.
#
# Where does everyone live?
#
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay,
# Liskov, Perlis, and Ritchie.

import itertools

def floor_puzzle():
  floors = range(1,6)
  fl_perm = list(itertools.permutations(floors))
  def top(fl): return fl == len(floors)
  def bottom(fl): return fl == 1
  def above(fl1,fl2): return fl1>fl2
  def adjacent(fl1,fl2): return abs(fl1-fl2) == 1

  for (Hopper, Kay, Liskov, Perlis, Ritchie) in fl_perm:
    if not top(Hopper) and not bottom(Kay) and not bottom(Liskov) and not top(Liskov) and above(Perlis,Kay) and not adjacent(Ritchie,Liskov) and not adjacent(Liskov, Kay):
      return [Hopper, Kay, Liskov, Perlis, Ritchie]

print floor_puzzle()