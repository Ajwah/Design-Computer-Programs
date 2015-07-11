"I learned about docstrings which can be used to document code. See docstrings.py for more info"

"The function split() converts a string into a list of characters"
sf = "6C 7C 8C 9C TC".split()

"To create a list of 100 occurences of something, you can multiply and add"
"This syntax will create a list encompasing 100 other lists"
print [sf] + 99*[sf]
"This syntax will create one list of a hundred repetitions of the sequence contained in sf"
print 99*sf

"This syntax allows for a very short and efficient conversion of string values to numbers"
h1 = "6C 7C 8C 9C TC".split()
h2 = ['AC', '3D', '4S', 'KH']
print ["--23456789TJQKA".index(r) for r,s in h1]
print ["--23456789TJQKA".index(r) for r,s in h2]

def flush(hand):
    "Return True if all the cards have the same suit."
    """My original implementation as follows:
      s = ''.join([s for r,s in hand])
      return s == "CCCCC" or s == "SSSSS" or s == "DDDDD" or s == "HHHHH"

      However, the implementation of the instructor is a lot better:
    """
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

h1 = "6C 7C 8C 9C TC".split()
h2 = ['AD', '3D', '4D', 'KD']
print flush(h1)
print flush(h2)

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    """
      I retained my original implementation, however this one is cool as well:
      return max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5
    """
    # Your code here.
    return 5*ranks[0] == sum(ranks) + 10 and len(ranks) == 5

print straight([9, 8, 7, 6, 5])


def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    """My original implementation which I prefer over the instructor's
    one which utilized a for loop instead"""
    return reduce(lambda a,x: x if (ranks.count(x) == n) else a, ranks, None)
print kind(3, [9, 8, 7, 9, 8])
