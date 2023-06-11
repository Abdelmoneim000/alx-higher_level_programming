#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        counter = my_list[0]
        for i in my_list:
            if i > counter:
                counter = i
            else:
                continue
        return counter
