#!/usr/bin/python3
# Function that checks if character is lowercase
def islower(c):
    # Check if character is between 'a' and 'z'
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False
