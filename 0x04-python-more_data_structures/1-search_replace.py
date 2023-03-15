#!/usr/bin/python3

def search_replace(my_list, search, replace):
    newList = []
    for i in my_list:
        if i == search:
            i = replace
            newList.append(i)
        else:
            newList.append(i)
    return newList
