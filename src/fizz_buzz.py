def fizz_buzz(param):
  #Type your code here
  if param % 3 == 0 and param % 5 == 0:
      return "FizzBuzz"
  if param % 3 == 0:
      return "Fizz"
  if param % 5 == 0:
      return "Buzz"
  if param % 3 != 0 and param % 5 != 0:
      return str(param)




