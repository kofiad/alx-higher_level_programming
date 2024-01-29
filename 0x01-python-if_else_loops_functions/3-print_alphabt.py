#!/usr/bin/python3
for alphabet in range(97, 123):
    if chr(alphabet) not in ['e', 'q']:
        print("{}".format(chr(alphabet)), end="")
