#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    for x in my_list:
        if x not in new_list:
            new_list.append(x)
    for x in new_list:
        sum += x
    return (sum)
