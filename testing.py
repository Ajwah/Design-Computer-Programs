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

print bcolors.FAIL + "Warning: No active frommets remain. Continue?" + bcolors.ENDC


