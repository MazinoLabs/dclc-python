# Dictionaries Exercises
#Exercises

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}

print(f"Original dictionary: {my_dict}")
my_dict["profession"] = "Doctor"
print(f"Updated dictionary after adding 'profession': {my_dict}")

my_dict["age"] = 40
print(f"Updated dictionary after modification:  {my_dict}")

print(f"City: {my_dict.get("city")}")


#Exercise 2
my_dict = {'name': 'Alice', 'age': 35,
           'city': 'New York', 'profession': 'Doctor'}

print(my_dict)

my_dict.pop("profession")
print(f"pdated dictionary after removing 'profession': {my_dict} \n")

print("Printing all key-value pairs:")
for key, val in my_dict.items():
    print(f"{key} : {val}")


def check_in_dict(kvp: dict, key):
    if kvp.get(key):
        return True
    else:
        return False


print(f"Does Key exist? {check_in_dict(kvp=my_dict, key='age')}")

# Exercise 3
def make_dict(key: list, val: list):
    new_dict = {}
    for x in range(0, len(key)):
        new_dict[key[x]] = val[x]
    print(new_dict)


def make_new_dict(key: list, val: list):
    print(dict(zip(key, val)))


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

make_new_dict(keys, values)


#Exercise 4
def clear_dict(a_dict: dict):
    a_dict.clear()
    return a_dict


my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
print(clear_dict(my_dict))

#Exercise 5
def merge_dict(dict_1: dict, dict_2: dict):
    dict_1.update(dict_2)
    print(dict_1)


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

merge_dict(dict1, dict2)

#Exercise 6
def count_char(word):
    new_dict = {}
    for ch in word:
        new_dict[ch] = word.count(ch)
    print(new_dict)


string1 = 'Jessa'
count_char(string1)


# Exercise 7
data = {'person': {'name': 'Alice', 'age': 30}}

print(f"{data['person']['name']}'s age is: {data['person']['age']}")


#Exercise 8
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict["class"]["student"]["marks"]["history"])


#Exercise 9
nested_student_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
nested_student_dict["class"]["student"]["name"] = "Jessa"

print(nested_student_dict)


#Exercise 10
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
new_dict = {}

for x in employees:
    new_dict[x] = defaults

print(new_dict)



#Tuple Exercises
#Exercise 1
my_tuple = (1, 2, 3, 4, 5)
print(f"My tuple: {my_tuple}")

print(f" The third element of my_tuple:{my_tuple[2]}")
print(f"The length of my_tuple: {len(my_tuple)}")


#Exercise 2
original_tuple = ('a', 'b')

new_tuple = original_tuple*3
print(new_tuple)



#Exercise 3
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(numbers[3:7])


#Exercise 4
tuple1 = (10, 20, 30, 40, 50)
arr = []
for x in range(len(tuple1)-1, -1, -1):
    arr.append(tuple1[x])
new_tuple = tuple(arr)
print(new_tuple)



#Exercise 5
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

print(tuple1[1][1])



#Exercise 6
new_tuple = (50,)
print(new_tuple)



#Exercise 7
tuple1 = (10, 20, 30, 40)

a, b, c, d = tuple1

print(a)
print(b)
print(c)
print(d)



#Exercise 8
tuple1 = (11, 22)
tuple2 = (99, 88)
print(f"tuple1 = {tuple1}")
print(f"tuple2 = {tuple2}\n")
arr = tuple2
tuple2 = tuple1
tuple1 = arr

print(f"tuple1 = {tuple1}")
print(f"tuple2 = {tuple2}")



#Exercise 9
tuple1 = (11, 22, 33, 44, 55, 66)

tuple2 = tuple(tuple1[3:5])

print(tuple2)



#Exercise 10
my_list = [10, 20, 30]
my_tuple = tuple(my_list)
print(my_tuple)

