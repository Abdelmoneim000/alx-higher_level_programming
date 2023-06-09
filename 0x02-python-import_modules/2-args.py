#!/usr/bin/python3
if __name__ == "__main__" :
    from sys import argv
    leng = len(argv) -1
    
    numb = 1
    
    for i in argv:
        if i == argv[0]:
            print("{0} arguments:".format(leng))
        else:
            print("{0}: {1}".format(numb, i))
            numb += 1
