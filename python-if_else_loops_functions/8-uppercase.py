#!/usr/bin/python3
# Function that prints string in uppercase
def uppercase(str):
    # Loop through each character in string
    for c in str:
        # Check if character is lowercase
        if ord(c) >= 97 and ord(c) <= 122:
            # Convert lowercase to uppercase using ASCII difference
            c = chr(ord(c) - 32)

        # Print each character without a newline
        print("{}".format(c), end="")

    #Print newline at end
    print()
