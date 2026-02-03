# Exercise 1: Calculate the multiplication and sum of two numbers
def sum_or_product(a, b):
    return a*b if a*b <= 1000 else a+b


num_1 = int(input("Enter the First Number"))
num_2 = int(input("Enter the First Number"))
print(sum_or_product(num_1, num_2))


# Exercise 2: Print the Sum of a Current Number and a Previous number
def summation(num):
    prev_num = 0
    for x in range(num):
        print(f"Current Number{x}Previous Number {prev_num}  Sum:{x+prev_num}")
        prev_num = x


user_num = int(input("Enter the Number you want to sum up"))
summation(user_num)


# Exercise 3: Print characters present at an even index number
def even_index(word):
    for x in range(len(word)):
        if x % 2 == 0:
            print(word[x])


phrase = input("Enter the Phrase")
even_index(phrase)


# Exercise 4: Remove first n characters from a string
def remove_chars(word, n):
    return word[n:]


word = input("Enter the word")
num_char = int(input("How many character should be removed"))
print(remove_chars(word, num_char))


#Exercise 5: Check if the first and last numbers of a list are the same
def check_if_same(arr):
    first = arr[0]
    last = arr[len(arr)-1]
    return True if first == last else False


print(check_if_same([75, 65, 35, 75, 30]))
print(check_if_same([45, 5, 33, 14, 45]))


# Exercise 6: Display numbers divisible by 5
def div_by_five_list(arr):
    for x in arr:
        if x % 5 == 0:
            print(x)


div_by_five_list([10, 20, 33, 46, 55])
div_by_five_list([3, 25, 40, 44, 60])


# Exercise 7: Find the number of occurrences of a substring in a string
def count_occurence(phrase, find):
    return f"{find} was found {phrase.count(find)} times"


print(count_occurence("Emma is good developer. Emma is a writer", "Emma"))


# Exercise 8: Print the following pattern
def num_pyramid(n):
    for x in range(n+1):
        print((str(x)+" ")*x)


num_pyramid(5)


# Exercise 9: Check Palindrome Number
def check_palidrome(num):
    number = str(num)
    rev_num = ""
    for x in range(len(number)-1, -1, -1):
        rev_num += number[x]
    return f"Yes. {number} is palindrome number" if number == rev_num else f"No. {number} is not palindrome number"


print(check_palidrome(125))
print(check_palidrome(121))


#Exercise 10: Merge two lists using the following condition
def merge_lists(arr1, arr2):
    new_arr = []
    for x in arr1:
        if x % 2 != 0:
            new_arr.append(x)
    for x in arr2:
        if x % 2 == 0:
            new_arr.append(x)
    return new_arr


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

print(merge_lists(list1, list2))


# Exercise 11: Get each digit from a number in the reverse order.
def rev_number(num):
    number = str(num)
    rev_num = ""
    for x in range(len(number)-1, -1, -1):
        rev_num += number[x] + " "
    return rev_num


print(rev_number(7536))
print(rev_number(12345))


# Exercise 12: Calculate income tax
def tax_calculation(income):
    tax = 0
    if income > 20000:
        tax = 10000*0.1 + (income-20000)*0.2
    elif 10000 < income <= 20000:
        tax = (income-10000)*0.1
    else:
        tax = 0
    return tax


print(tax_calculation(15000))


#Exercise 13: Print multiplication table from 1 to 10
for x in range(1, 11):
    for y in range(1, 11):
        print(x*y, end=" ")
    print("\t\t")
