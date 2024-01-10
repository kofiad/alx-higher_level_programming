#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result_list = my_list[:]
    for i in range(len(result_list)):
        if result_list[i] == search:
            result_list[i] = replace
    return result_list
