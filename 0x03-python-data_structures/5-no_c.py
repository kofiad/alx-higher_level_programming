#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for a in my_string:
        if a.lower() != 'c':
            new_string += a
    return (new_string)
