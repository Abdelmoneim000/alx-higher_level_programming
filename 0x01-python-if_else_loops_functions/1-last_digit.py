#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = str(number)
n = str1[-1]
reint = int(n)

if number < 0:
    reint = reint * -1

if reint > 5:
    print("Last digit of %d is %d and is greater than %d" %
          (number, reint, 5))
elif reint < 6 and reint != 0:
    print("Last digit of %d is %d and is less than %d and not %d" %
          (number, reint, 6, 0))
elif reint == 0:
    print("Last digit of %d is %d and is %d" % (number, reint, 0))
