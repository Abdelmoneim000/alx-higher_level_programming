#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence):
        new_t = (len(sentence), sentence[0])
    else:
        new_t = (0, "None")
    return new_t
