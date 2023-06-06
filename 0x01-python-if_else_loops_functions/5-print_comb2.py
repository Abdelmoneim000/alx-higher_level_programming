#!/usr/bin/python3
for i in range(0, 100):
    i = str(i)
    if int(i) < 10:
        i = "0" + i
    if i == "99":
        print("{}\n".format(i), end='')
    else:
        print("{}, ".format(i), end='')
