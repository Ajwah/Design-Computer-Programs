import itertools
from poker import *

class bcolors:
		HEADER = '\033[95m'
		OKBLUE = '\033[94m'
		OKGREEN = '\033[92m'
		WARNING = '\033[93m'
		FAIL = '\033[91m'
		ENDC = '\033[0m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'

def best_hand(hand):
		"From a 7-card hand, return the best 5 card hand."
		return max(itertools.combinations(hand, 5), key=hand_rank)

def test_best_hand():
		assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
						== ['6C', '7C', '8C', '9C', 'TC'])
		assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
						== ['8C', '8S', 'TC', 'TD', 'TH'])
		assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
						== ['7C', '7D', '7H', '7S', 'JD'])
		return "test_best_hand passes"

"""
This is my personal implementation which I relinquish for the elegance of the solution provided.
def best_wild_hand(hand):
  def all_possible_replaces(hand):
    deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
    for i in hand:
      if i != '?B' and i != '?R': deck.remove(i)
    bd = filter(lambda x: x[1] == "C" or x[1] == "S", deck) if '?B' in hand else ['--']
    rd = filter(lambda x: x[1] == "H" or x[1] == "D", deck) if '?R' in hand else ['--']
    return (bd,rd)

  bd, rd = all_possible_replaces(hand)
  reduced = filter(lambda i: i != '?B' and i != '?R', hand)
  biggest_hands = [max(itertools.combinations(reduced + [i] + [j], 5), key=hand_rank) for i in bd for j in rd]
  biggest = max(biggest_hands, key=hand_rank)

  return biggest
"""
def best_wild_hand(hand):
  allranks = '23456789TJQKA'
  redcards = [r+s for r in allranks for s in 'HD']
  blackcards = [r+s for r in allranks for s in 'SC']

  def replacements(card):
    "Return a list for possible replacements of a card"
    if card == '?B': return blackcards
    if card == '?R': return redcards
    else: return [card]

  hands = set(best_hand(h)
              for h in itertools.product(*map(replacements,hand)))
  return max(hands, key=hand_rank)



def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'

print test_best_wild_hand()

