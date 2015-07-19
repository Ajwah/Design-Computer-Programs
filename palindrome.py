# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    "Return (i, j+1) such that text[i:j] is the longest palindrome in text."
    ln = len(text)-1
    def compare(i,j): return (text[i].lower() == text[j].lower())
    def palindrome(i,j,t):
      print (i,j,text[i:j+1],t)
      if i < 0 or j > ln:
        if compare(ln-1,ln):
          return (ln-1,ln)
        else:
          return (0,0)
      if compare(i,j):
        if i == 0 and t == 0:
          palin = palindrome(i,j+1,t)
        else:
          palin = palindrome(i-1,j+1,t)
        return ((i,j) if (j-i > palin[1]-palin[0]) else palin)
      elif compare(i,i+1):
       return (i,i+1)
      else:
        return palindrome(t+1,t+3,t+1)
      return (i,j)

    if ln == -1:
      return (0,0)
    elif ln == 0:
      return (0,1)
    else:
     r = palindrome(0,2,0)
    return (r[0],r[1]+1)

def test():
    L = longest_subpalindrome_slice
    assert L('') == (0, 0)
    assert L('r') == (0, 1)
    assert L('ra') == (0, 1)
    assert L('rr') == (0, 2)
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('abcdefghijklmo') == (0,1)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()