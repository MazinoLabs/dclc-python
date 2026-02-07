# Exercise 1: List Creation using two lists

def odd_even_list(arr1: list, arr2: list):
    new_list = []
    for num in arr1:
        if arr1.index(num) % 2 != 0:
            new_list.append(num)
    for num in arr2:
        if arr2.index(num) % 2 == 0:
            new_list.append(num)

    return new_list

# Excercise 2: Remove the fourth element and add it to the second position and at the end of the list


def remove_fourth_append_second(arr: list):
    x = arr[4]
    print(f"Original List {arr}")
    arr.remove(x)
    print(f"List After removing element at index 4 {arr}")
    arr.insert(2, x)
    print(f"List after Adding element at index 2 {arr}")
    arr.append(x)
    print(f"List after Adding element at last  {arr}")


# Slice list into 3 equal chunks and reverse each chunk
def split_list(arr: list):
    start = 0
    end = 3
    for x in range(start, len(arr), 3):
        chunk = arr[start:end]
        print(f"Chunk {(x // 3)+1} {chunk}")
        chunk.reverse()
        print(f"After Reversing it: {chunk}")

        start = end
        end += 3


# Exercise 4: Count the occurrence of each element from a list
def count_occurrence(arr: list):
    out = ""
    for num in arr:
        out += f"{num}:{arr.count(num)}, "

    print("Printing count of each item {" + out + " }")


# Exercise 5: Paired Elements from Two Lists as a Set
def list_as_set(arr1: list, arr2: list):
    print(f"Result is {set(zip(arr1, arr2))}")


# Exercise 6: Set Intersection and Removal
def intersect(arr1: set, arr2: set):
    intersection_arr = arr1.intersection(arr2)
    arr1 = arr1.difference(intersection_arr)
    arr2 = arr2.difference(intersection_arr)
    print(f"Intersection is {intersection_arr}")
    print(f"First Set after removing common element {arr1}")
    print(f"Second Set after removing common element {arr2}")


# Exercise 7: Subset or Superset of another set
def sub_sup_set(set_1: set, set_2: set):
    print(f"First set is subset of second set - {set_1.issubset(set_2)}")
    print(f"Second set is subset of First set -  {set_2.issubset(set_1)}")

    print(f"First set is Super set of second set - {set_1.issuperset(set_2)}")
    print(f"Second set is Super set of First set - {set_2.issuperset(set_1)}")

    print(f"First Set {"set()" if set_1.issubset(set_2) else set_1}")
    print(f"Second Set  {set_2.clear() if set_2.issubset(set_1) else set_2}")


# Exercise 8: Filter List Against Dictionary Values
def map_list_to_dict(arr: list, mapping: dict):
    removed_arr = []
    for x in arr:
        for y in mapping.values():
            if x == y:
                removed_arr.append(x)
    print(f"After removing unwanted elements from list {removed_arr}")

# Exercise 9: Extract Unique Dictionary Values to List


def make_list(mapping: dict):
    arr = []
    for x in mapping.values():
        if x not in arr:
            arr.append(x)
    print(arr)


# Exercise 10: remove duplicates from a list
def remove_dep_tuple(arr: list):
    unique_arr = []
    for x in arr:
        if x not in unique_arr:
            unique_arr.append(x)
    print(f"unique items {unique_arr}")
    print(f"Tuple {tuple(unique_arr)}")
    unique_arr.sort()
    print(f"Min {unique_arr[0]}")
    print(f"Max {unique_arr[-1]}")