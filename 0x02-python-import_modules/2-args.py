#!/usr/bin/python3
if __name__ == "__main__" :
    from sys import argv
    leng = len(argv) -1
    
    numb = 1
    
    if leng == 0:
        print("{0} arguments.".format(leng))
    elif leng == 1:
        print("{0} argument:\n{1}: {2}".format(leng, numb, argv[numb]))
    else:
        print("{0} arguments:".format(leng))
        for i in argv:
            if i == argv[1]:
                continue
            else:
                print("{0}: {1}".format(numb, argv[numb]))
                numb += 1
