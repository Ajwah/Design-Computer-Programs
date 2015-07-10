"I learned about docstrings which can be used to document code. See docstrings.py for more info"

"The function split() converts a string into a list of characters"
sf = "6C 7C 8C 9C TC".split()

"To create a list of 100 occurences of something, you can multiply and add"
"This syntax will create a list encompasing 100 other lists"
print [sf] + 99*[sf]
"This syntax will create one list of a hundred repetitions of the sequence contained in sf"
print 99*sf
