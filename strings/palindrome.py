"""
As the name suggests, this module contains functions to check if a string is a palindrome.
A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
For example "madam", "sos", "lol",  "A man, a plan, a canal - Panama" are palindromes.
"""
import string
def is_palindrome(str):

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
    #convert to lowercase
    str = str.lower()
    #check if the string is equal to its reverse
    return str == str[::-1]

"""
# Example usage
print(is_palindrome("A man, a plan, a canal - Panama"))

"""