"Implementation of a poker game"
def poker(hands):
  "Return the best hand: poker([hand,...]) => hand"
  """The way max works here is by applying the function hand_rank over every hand in hands.
  This function in turn returns a tuple, the first element of which is an int betwen 0-8.
  By default, max will be done with regards to the first element. Only in case of match,
  the second element will be considered.
  More info: http://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression
  """
  return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
  m = max(iterable, key=key)
  return filter(lambda d: d == m, iterable)

def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ["--23456789TJQKA".index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return [5,4,3,2,1] if ranks == [14,5,4,3,2] else ranks

def hand_rank(hand):
  "Determine the rank of the card"
  """
  full flush : 8, highest
  four aces and a queen kicker: (7,14,q=12)
  full house, eight over kings: (6, 8, 13)
  flush 10, 8 (3 succeeding cards by -2): (5,[10,8,7,5,3])
  straight jack high : (4,11)
  three sevens: (3,7,[7,7,7,5,2])
  two pair, jacks and threes: (2,11,3,[13,11,11,3,3])
  pair of two's, jack high: (1,2,[11,6,3,2,2])
  nothing: (0,7,5,4,3,2)
  """
  ranks = card_ranks(hand)
  if straight(ranks) and flush(hand):            # straight flush
      return (8, max(ranks))
  elif kind(4, ranks):                           # 4 of a kind
      return (7, kind(4, ranks), kind(1, ranks))
  elif kind(3, ranks) and kind(2, ranks):        # full house
      return (6, kind(3, ranks), kind(2, ranks))
  elif flush(hand):                              # flush
      return (5, ranks)
  elif straight(ranks):                          # straight
      return (4, max(ranks))
  elif kind(3, ranks):                           # 3 of a kind
      return (3, kind(3, ranks), ranks)
  elif two_pair(ranks):                          # 2 pair
      return (2, two_pair(ranks)[0],
                 two_pair(ranks)[1],
                 ranks)
  elif kind(2, ranks):                           # kind
      return (1, kind(2, ranks), ranks)
  else:                                          # high card
      return (0, ranks)

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return 5*ranks[0] == sum(ranks) + 10 and len(ranks) == 5

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    return reduce(lambda a,x: x if (ranks.count(x) == n) else a, list(reversed(ranks)), None)

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    h = kind(2, ranks)
    l = kind(2, list(reversed(ranks)))
    return (h,l) if h>l else None

def test():
  "Test cases for the functions in poker program."
  sf = "6C 7C 8C 9C TC".split()
  fk = "9D 9H 9S 9C 7D".split()
  fh = "TD TC TH 7C 7D".split()
  tp = "5S 5D 9H 9C 6S".split() # Two pairs
  fkranks = card_ranks(fk)
  tpranks = card_ranks(tp)
  al = "AC 2D 4H 3D 5S".split() # Ace-Low Straight
  assert straight(card_ranks(al)) == True
  assert kind(4, fkranks) == 9
  assert kind(3, fkranks) == None
  assert kind(2, fkranks) == None
  assert kind(1, fkranks) == 7
  assert card_ranks(sf) == [10,9,8,7,6]
  assert card_ranks(fk) == [9,9,9,9,7]
  assert card_ranks(fh) == [10,10,10,7,7]
  assert straight([9, 8, 7, 6, 5]) == True
  assert straight([9, 8, 8, 6, 5]) == False
  assert flush(sf) == True
  assert flush(fk) == False
  assert poker([sf,fk,fh]) == [sf], "Assert that straight flush is the winning hand"
  assert poker([fk,fh]) == [fk], "Assert that four of a kind is the winning hand"
  assert poker([fh,fh]) == [fh, fh], "Assert that two times full house produces full house as the winning hand"
  assert poker([fk]) == [fk], "Assert that one player always has the winning hand"
  assert poker(100*[sf]) == 100*[sf]
  assert poker([sf] + 99*[fk]) == [sf]

  return "tests pass."
print test()