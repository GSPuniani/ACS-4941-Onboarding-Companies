"""
Problem:
Given a string of digits 2 to 9 a user has pressed on a T9 “old school” telephone keypad, 
return a list of all letter combinations they could have been trying to type on the keypad.
"""

"""
Strategy: Save each digit as a key and a list of corresponding letters as a value in a dictionary, 
then recursively iterate through all possible combos"""

KEYPAD_DICT = {
  "2": ["a", "b", "c"],
  "3": ["d", "e", "f"],
  "4": ["g", "h", "i"],
  "5": ["j", "k", "l"],
  "6": ["m", "n", "o"],
  "7": ["p", "q", "r", "s"],
  "8": ["t", "u", "v"],
  "9": ["w", "x", "y", "z"]
}

def t9_letters(digits_str):
  return 