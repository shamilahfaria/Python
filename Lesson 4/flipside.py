# flipside
def flipside(s):
  """
  input: a string s
  output: a string, x, whose first half is s's second half and whose second half is s's first half
    s strings of odd length are divided so that s's first "half" is one letter shorter than its second
  """
  # find the halfway point of the original string, s. whole numbers only
  halfway = len(s)//2
  # create a new string that stores from the halfway point to the end of string s (inclusive) and appends from the first up to the halfway point (exclusive)
  x = s[halfway:len(s)]+s[:halfway] # string slicing: inclusive of starting index, exclusive of ending
  # return the new string
  return x


# Tests below, do not change
assert flipside('carpets') == 'petscar', f"Reported {flipside('carpets')} for flipside('carpets') instead of petscar"
assert flipside('homework') == 'workhome', f"Reported {flipside('homework')} for flipside('homework') instead of workhome"
assert flipside('ada') == 'daa', f"Reported {flipside('daa')} for flipside('ada') instead of daa"

# If the program gets here, the code works!
print("Your solution works!")