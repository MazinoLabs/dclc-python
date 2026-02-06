# Exercise 1: List Creation using two lists

def odd_even_list(list1, list2):
    new_list = []
    for num in list1:
        if list1.index(num) % 2 != 0:
            new_list.append(num)
    for num in list2:
        if list2.index(num) % 2 == 0:
            new_list.append(num)

    return new_list
