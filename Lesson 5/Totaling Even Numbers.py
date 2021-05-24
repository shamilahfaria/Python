def total_even_numbers(num):
    """
    input: an integer, num
    output: sum of all even numbers from 0 to num, inclusive
    """
    sum = 0 #initializing sum
    # Your code goes here
    # add every second number up to and including num to sum
    x = 0 # variable to store every second number from 0 up to num
    while x <= num:
      sum += x
      x += 2

    # End of your code
    return sum

# Tests below, do not change
assert total_even_numbers(6) == 12, f"Reported {total_even_numbers(6)} for total_even_numbers(6) instead of 12"
assert total_even_numbers(0) == 0, f"Reported {total_even_numbers(0)} for total_even_numbers(0) instead of 0"
assert total_even_numbers(1) == 0, f"Reported {total_even_numbers(1)} for total_even_numbers(1) instead of 0"
assert total_even_numbers(15) == 56, f"Reported {total_even_numbers(15)} for total_even_numbers(15) instead of 56"

# If the program gets here, the code works!
print("Your solution works!")