import random

# Create an empty dictionary 'var'.
var = {}

# Print the content of 'var' (which is an empty dictionary).
print(var)

# Print the data type of 'var' (a dictionary).
print(type(var))

# Create a dictionary 'var2' with key-value pairs.
var2 = {"juice": "cranberry", "movie": "The Lion King", "fruit": "mango"}

# Print the content of 'var2'.
print(var2)

# Print the value associated with the key "movie" in 'var2'.
print(var2["movie"])

# Create a dictionary 'var3' with an integer (0) as a key (not recommended).
var3 = {0: "number"}  # Avoid using integer indexes in dictionaries.

# Print the content of 'var3'.
print(var3)

# Print the value associated with the integer key 0 in 'var3'.
print(var3[0])

# Add a new key-value pair "drank": "Petron" to 'var2'.
var2["drank"] = "Petron"

# Print the updated 'var2'.
print(var2)

# Update the value associated with the key "juice" in 'var2'.
var2["juice"] = "apple"

# Print the updated 'var2'.
print(var2)

# Delete the key "drank" and its associated value from 'var2'.
del var2["drank"]

# Print 'var2' after deleting the key-value pair.
print(var2)

# Print the list of available methods/functions for 'var2'.
print(dir(var2))

# Print a list of keys in 'var2'.
print(list(var2.keys()))

# Print a list of values in 'var2'.
print(list(var2.values()))

# Iterate through key-value pairs in 'var2' and print them.
for k, v in var2.items():
    print(k, v)
    
# Create a dictionary of lists 'dict_of_lists'.
dict_of_lists = {}
dict_of_lists["first"] = [0, 1, 2]
dict_of_lists["second"] = [0, 1, 2]
dict_of_lists["third"] = [0, 1, 2]

# Iterate through key-value pairs in 'dict_of_lists'.
for k, v in dict_of_lists.items():
    print(k, v, type(v))
    # Iterate through elements in each list and print them.
    for element in v:
        print(element)

# Create a dictionary 'second_dict_of_lists' using dictionary comprehension.
# Initialize each key with a list containing the values [0, 1, 2].
second_dict_of_lists = {key: [0, 1, 2] for key in ["first", "second", "third"]}
