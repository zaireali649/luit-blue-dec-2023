import random

# Generate a random integer between 0 and 10, inclusive.
number = random.randint(0, 10)

# The following lines have been commented out for specific reasons:
# print("Hello")  # This line has a syntax error. Unexpected Indent
# 1/0  # This line will cause a runtime error. Can't compute a valid syntax instruction

# Set a threshold for comparison.
threshold = 6
threshold2 = 4

# Check if the generated number is less than the first threshold.
if number < threshold:
    print("Small Number")
# If not, check if it's greater than the first threshold.
elif number > threshold:
    print("Big Number")
else:  # If it's equal to the first threshold:
    print("Number is", threshold)

# Check if the generated number is less than the second threshold.
if number < threshold2:
    print("Really Small Number")

# Print "dedented" to indicate the end of this section.
print("dedented")

# Print the randomly generated number.
print(number)
