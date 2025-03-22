# This is the Utility functions where we store all the helper functions
def find_max(numbers):
     maximum = numbers[0]
     for number in numbers:
          if number > maximum:
               maximum = number
     return maximum
 