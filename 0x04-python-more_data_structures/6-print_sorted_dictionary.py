#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_list = list(a_dictionary.keys())
    sorted_keys = sorted(keys_list)
    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")
