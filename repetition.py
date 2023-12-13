import random

# Generate a random number between 0 and 10 (inclusive).
number = random.randint(0, 10)

# Initialize a counter for the while loop.
counter = 0

# Start a while loop that continues until 'number' is equal to 7 or the counter reaches 13.
while number != 7:
    # Generate a new random number.
    number = random.randint(0, 10)
    # Increment the counter by 1.
    counter = counter + 1  # counter += 1

    # Check if the counter has reached 13 or more, and break out of the loop if so.
    if counter >= 13:
        break

# Print the counter and the final value of 'number'.
print(counter, number)

# for loop

# Iterate through the numbers from 0 to 9 using a for loop.
for i in range(10):
    # Check if the square of 'i' is less than 50.
    if i**2 < 50:
        # If so, print 'i' and the square of 'i'.
        print(i, i**2)
    else:
        # If the square of 'i' is greater than or equal to 50, break out of the loop.
        break

# Print the final value of 'i' after the loop exits.
print(i)
