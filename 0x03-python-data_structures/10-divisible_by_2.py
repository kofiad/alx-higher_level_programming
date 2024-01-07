#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_list = []
    for i in my_list:
        multiple_2 = i % 2 == 0
        div_list.append(multiple_2)
    return (div_list)
