"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from collections import Counter

def frequencies(items):
    frequencies = {}
    # Your code goes here
    #loop through each item object in items list
    for item in items:
        #if item is not a string, convert item into string 
        key = str(item) if not isinstance(item, str) else item

        frequencies[key] = frequencies.get(key, 0) + 1
    return frequencies
