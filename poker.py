"Implementation of a poker game"
def poker(hands):
  "Return the best hand: poker([hand,...]) => hand"
  return max(hands,hand_rank)

def hand_rank(hands):
  "Determine the rank of all the cards involved in hands"
  return None

def test():
  "Test cases for the functions in poker program."
  sf = "6C 7C 8C 9C TC".split()
  fk = "9D 9H 9S 9C 7D".split()
  fh = "TD TC TH 7C 7D".split()
  assert poker([sf,fk,fh]) == sf, "Assert that straight flush is the winning hand"
  assert poker([fk,fh]) == fk, "Assert that four of a kind is the winning hand"
  assert poker([fh,fh]) == fh, "Assert that two times full house produces full house as the winning hand"
  assert poker([fk]) == fk, "Assert that one player always has the winning hand"
  assert poker([fh,fh]) == fh, "Assert that two times full house produces full house as the winning hand"
  assert poker([sf for x in xrange(0,100)]) == sf
  assert poker([sf] + 99*[fk]) == sf
  return "tests pass."

print test()
