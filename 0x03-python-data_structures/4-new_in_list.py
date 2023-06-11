#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_new = []
    for i in my_list:
        list_new.append(i)
    if idx > len(my_list) - 1 or idx < 0:
        return list_new
    else:
        list_new[idx] = element
        return list_new
