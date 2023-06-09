#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    my_func = [add, sub, mul, div]
    operator = ["+", "-", "*", "/"]
    index = 0
a = 10
b = 5

for i in my_func:
    print("{0} {1} {2} = {3} ".format(a, operator[index], b, i(a, b)))
    index += 1
