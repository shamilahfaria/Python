# checkends
def checkends(s):
    """
    input: a string s
    output: False if the first and last character of the string are different,
        True otherwise.
    """
    # checks if the first character in the string is equal to the last character
    if s[0]==s[-1]:
      return True
    else:
      return False

# Tests below, do not change
assert checkends('no match') == False, f"Reported {checkends('no match')} for checkends('no match') instead of False"
assert checkends('hah! a match') == True, f"Reported {checkends('hah! a match')} for checkends('hah! a match') instead of True"
assert checkends('q') == True, f"Reported {checkends('q')} for checkends('q') instead of True"
assert checkends(' ') == True, f"Reported {checkends(' ')} for checkends(' ') instead of True"
assert checkends('!ada!') == True, f"Reported {checkends('!ada!')} for checkends('!ada!') instead of True"

# If the program gets here, the code works!
print("Your solution works!")