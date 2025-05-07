"""
This program counts the number of uppercase and lowercase letters in a given string.
It uses the isupper() and islower() methods to check the case of each character.
The program iterates through each character in the string and increments the respective counters.
The final counts are printed at the end.
"""

def count_upper_lower(string):
    """
    Count the number of uppercase and lowercase letters in a string.
    
    Parameters:
    string (str): The input string to be analyzed.
    
    Returns:
    tuple: A tuple containing the count of uppercase and lowercase letters.
    """
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        else:
            pass
    # Ignore non-alphabetic characters

    return upper_count, lower_count


"""
Example usage:
t=count_upper_lower("Hello World!")
print(t)


You can also add a print statement in case you need to see the output directly.
print("Uppercase letters:", t[0])
print("Lowercase letters:", t[1])

"""