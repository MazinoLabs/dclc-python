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

#Excercise 2: Remove the fourth element and add it to the second position and at the end of the list
def remove_fourth_append_second(arr):
    x = arr[4]
    print(f"Original List {arr}")
    arr.remove(x)
    print(f"List After removing element at index 4 {arr}")
    arr.insert(2, x)
    print(f"List after Adding element at index 2 {arr}")
    arr.append(x)
    print(f"List after Adding element at last  {arr}")