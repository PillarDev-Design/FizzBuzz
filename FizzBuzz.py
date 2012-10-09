# Declare Variable
x = 1

# Function to print (Strictly just a formatting idea)
def print_x(number, word):
    if (number == 100):
        print '(%s) %s' % (number, word)
    elif (number < 10):
        print '(00%s) %s' % (number, word)
    elif (number < 100):
        print '(0%s) %s' % (number, word)

# Loop Until 100
while x < 101:
    # Divisible by 3 and 5?
    if (x%3 == 0) and (x%5 == 0):
        print_x(x, "FizzBuzz")

    # Divisible by 3?
    elif x%3 == 0:
        print_x(x, "Fizz")

    # Divisible by 5?
    elif x%5 == 0:
        print_x(x, "Buzz")

    # Not divisible by 3 or 5
    else:
        print_x(x, "")

    # Increment the Variable
    x += 1
