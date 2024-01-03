#!/usr/bin/python3
def fizzbuzz():
    for num in range(0, 101):
        if num % 3 == 0:
            print("Fizz".format(number), end=' ')
        elif num % 5 == 0:
            print("Buzz".format(number), end=' ')
        elif num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz".format(number), end=' ')
        else:
            print("{}".format(number), end=' ')
