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
