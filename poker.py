"Implementation of a poker game"
def poker(hands):
  "Return the best hand: poker([hand,...]) => hand"
  return max(hands,hand_rank)

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = [r for r,s in cards]
    ranks.sort(reverse=True)
    return ranks

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

def test():
  "Test cases for the functions in poker program."
  sf = "6C 7C 8C 9C TC".split()
  fk = "9D 9H 9S 9C 7D".split()
  fh = "TD TC TH 7C 7D".split()
  assert card_ranks(sf) == [10,9,8,7,6]
  assert card_ranks(fk) == [9,9,9,9,7]
  assert card_ranks(fh) == [10,10,10,7,7]
  assert poker([sf,fk,fh]) == sf, "Assert that straight flush is the winning hand"
  assert poker([fk,fh]) == fk, "Assert that four of a kind is the winning hand"
  assert poker([fh,fh]) == fh, "Assert that two times full house produces full house as the winning hand"
  assert poker([fk]) == fk, "Assert that one player always has the winning hand"
  assert poker([fh,fh]) == fh, "Assert that two times full house produces full house as the winning hand"
  assert poker([sf for x in xrange(0,100)]) == sf
  assert poker([sf] + 99*[fk]) == sf
  return "tests pass."

print test()
