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

