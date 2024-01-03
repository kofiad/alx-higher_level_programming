#!/usr/bin/python3
def print_reverse_alphabet():
    lowStart = ord('z')
    upStart = ord('Y')
    for asciiValue in range(lowStart, ord('a') - 1, -1):
        print(chr(asciiValue), end='')
        if asciiValue > ord('a'):
            print(chr(asciiValue - (lowStart - upStart)), end='')
