def int_within_bounds(number, lower_bound, upper_bound):
  # Type your code
    if number % 1 != 0:
      return False
    if number >= lower_bound and number < upper_bound:
      return True
    else:
      return False




