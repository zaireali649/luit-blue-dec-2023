import random

# Create an empty list 'var'.
var = []

# Print the content of 'var' (which is an empty list).
print(var)

# Print the data type of 'var'.
print(type(var))

# Create a list 'var2' containing integers and a string.
var2 = [151, 251, 386, 493, 649, "009"]

# Print the content of 'var2'.
print(var2)

# Append an integer (721) to 'var2'.
var2.append(721)  # var2 = var2 + [721]

# Print the updated 'var2'.
print(var2)

# Print the list of available methods/functions for 'var2'.
print(dir(var2))

# Print the list of available methods/functions for the string "string".
print(dir("string"))

# Create a list 'var3' containing integers.
var3 = [0, 1, 2, 3, 4]

# Create a 'numbers' range object with values from 0 to 9.
numbers = range(10)

# Print the 'numbers' range.
print(numbers)

# Print the data type of 'numbers' (which is initially a range).
print(type(numbers))

# Convert 'numbers' to a list and print it.
numbers = list(numbers)
print(numbers)

# Print the element at index 4 of 'numbers'.
print(numbers[4])

# Reverse the order of elements in 'numbers' and print it.
numbers.reverse()
print(numbers)

# Print the element at index 4 of the reversed 'numbers'.
print(numbers[4])

# Find and print the index of the value 4 in 'numbers'.
print(numbers.index(4))

# Try to print the element at index 5, which does not exist (out of bounds).

# Reverse 'numbers' again and print it.
numbers.reverse()
print(numbers)

# Print the length (number of elements) of 'numbers'.
print(len(numbers))

# Iterate through 'numbers' and print the square of each number.
for number in numbers:
    print(number**2)

# Iterate through the numbers from 0 to 9 and print their cubes.
for i in range(10):
    print(i**3)

# Create a list 'list_of_lists' containing four lists with the same elements.
list_of_lists = []
list_of_lists.append([0, 1, 2])
list_of_lists.append([0, 1, 2])
list_of_lists.append([0, 1, 2])
list_of_lists.append([0, 1, 2])

# Print 'list_of_lists'.
print(list_of_lists)

# Iterate through 'list_of_lists' and print each element.
for list_element in list_of_lists:
    print(list_element)
    # Iterate through the elements of each sublist and print them.
    for element in list_element:
        print(element)

# Create a list of lists 'second_list_of_lists' using a list comprehension.
second_list_of_lists = [[0, 1, 2] for i in range(4)]

# Print 'second_list_of_lists'.
print(second_list_of_lists)
