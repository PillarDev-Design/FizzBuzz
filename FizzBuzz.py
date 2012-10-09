x = 1

while x < 101:
    if (x%3==0) and (x%5==0):
        if (x < 10):
            print '(00%s) FizzBuzz' % (x)
        elif (x < 100):
            print '(0%s) FizzBuzz' % (x)
        elif (x == 100):
            print '(%s) FizzBuzz' % (x)
    elif x%3==0:
        if (x < 10):
            print '(00%s) Fizz' % (x)
        elif (x < 100):
            print '(0%s) Fizz' % (x)
        elif (x == 100):
            print '(%s) Fizz' % (x)
    elif x%5==0:
        if (x < 10):
            print '(00%s) Buzz' % (x)
        elif (x < 100):
            print '(0%s) Buzz' % (x)
        elif (x == 100):
            print '(%s) Buzz' % (x)
    elif x < 101:
        if (x < 10):
            print '(00%s)' % (x)
        elif (x < 100):
            print '(0%s)' % (x)
        elif (x == 100):
            print '(%s)' % (x)

    x += 1
    if (x == 101):
        done = True
