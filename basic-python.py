# Exercise 1: Calculate the multiplication and sum of two numbers
def sum_or_product(a, b):
    return a*b if a*b <= 1000 else a+b


num_1 = int(input("Enter the First Number"))
num_2 = int(input("Enter the First Number"))
print(sum_or_product(num_1, num_2))