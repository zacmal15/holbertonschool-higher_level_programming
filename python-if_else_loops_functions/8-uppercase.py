#!/usr/bin/python3
# Function that prints a string in uppercase
def uppercase(str):
    # Loop through each character in string
    for c in str:
        # Check if character is lowercase
        if ord(c) >= 97 and ord(c) <= 122:
            # Convert lowercase to uppercase
            c = chr(ord(c) - 32)

        # Print character and newline only at end
        print("%c" % ord(c), end="" if c != str[-1] else "\n")
