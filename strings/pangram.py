"""
This script checks if a given string is a pangram.
A pangram is a sentence that contains every letter of the alphabet at least once.
For example, "The quick brown fox jumps over the lazy dog" is a pangram.
The script defines a function `is_pangram` that takes a string as input and returns True if it is a pangram, otherwise False.
"""
import string
def is_pangram(str, alphabet=string.ascii_lowercase):
    """
    Check if the input string is a pangram.
    
    Args:
        str (str): The input string to check.
        alphabet (str): The alphabet to check against. Default is lowercase English letters.
    
    Returns:
        bool: True if the string is a pangram, False otherwise.
    """
    #Convert alphabet to set
    alphabet = set(alphabet)

    #remove punctuation
    str = str.translate(str.maketrans("", "", string.punctuation))
    #remove digits
    str = str.translate(str.maketrans("", "", string.digits))
    #remove new line characters
    str = str.replace("\n", "")
    #remove tabs
    str = str.replace("\t", "")
    #remove carriage return
    str = str.replace("\r", "")
    #remove extra spaces
    str = str.replace("\r\n", "")
    str = str.replace("\n\r", "")
    str = str.replace(" ", "")
    
    # Convert the input string to lowercase and create a set of characters
    str_set = set(str.lower())
    
    # Check if all characters in the alphabet are present in the string set
    return ( str_set == alphabet)

"""
Example usage:
print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello World"))
print(is_pangram("Pack my box with - five dozen liquor jugs."))
"""