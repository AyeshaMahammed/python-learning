for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
# The FizzBuzz problem is a common coding challenge that tests basic programming skills.
# The task is to print numbers from 1 to 100, but for multiples of 3, print "Fizz" instead of the number,
# and for multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".
# This code uses a for loop to iterate through the numbers from 1 to 100.
# It uses the modulo operator (%) to check for divisibility by 3 and 5.
# The if-elif-else structure is used to determine what to print for each number.
# This code is a simple and effective solution to the FizzBuzz problem.
# It demonstrates the use of loops, conditionals, and basic arithmetic operations.
# The output will be the numbers from 1 to 100, with "Fizz", "Buzz", or "FizzBuzz" printed for the appropriate numbers.
# This code is a classic example of a programming interview question.
# It is often used to assess a candidate's understanding of loops and conditionals.
# The FizzBuzz problem is a common coding challenge that tests basic programming skills.