# Declare Variable
x = 1

# Loop Until 100
while x < 101:
    # Divisible by 3 and 5?
    if (x%3 == 0) and (x%5 == 0):
        if (x < 10):
            print '(00%s) FizzBuzz' % (x)
        elif (x < 100):
            print '(0%s) FizzBuzz' % (x)
        elif (x == 100):
            print '(%s) FizzBuzz' % (x)
    # Divisible by 3?
    elif x%3 == 0:
        if (x < 10):
            print '(00%s) Fizz' % (x)
        elif (x < 100):
            print '(0%s) Fizz' % (x)
        elif (x == 100):
            print '(%s) Fizz' % (x)
    # Divisible by 5?
    elif x%5 == 0:
        if (x < 10):
            print '(00%s) Buzz' % (x)
        elif (x < 100):
            print '(0%s) Buzz' % (x)
        elif (x == 100):
            print '(%s) Buzz' % (x)
    # Not divisible by 3 or 5
    elif x < 101:
        if (x < 10):
            print '(00%s)' % (x)
        elif (x < 100):
            print '(0%s)' % (x)
        elif (x == 100):
            print '(%s)' % (x)

    # Increment the Variable
    x += 1
