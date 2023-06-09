#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    numb = 1
    count = 0

    if len(argv) == 1:
        print("{0}".format(count))
    else:
        for i in argv:
            if i == argv[0]:
                continue
            count += int(i)
            numb += 1
        print("{0}".format(count))
