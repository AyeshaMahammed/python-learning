"""
This program gives a unique list of elements from a given list.
It uses a for loop to iterate through the list and add unique elements to a new list.
The program then prints the unique list.
"""
def unique_list(input_list):
    unique_elements = []
    for element in input_list:
        if element not in unique_elements:
            unique_elements.append(element)
    
    return unique_elements

"""
# Example usage
input_list = [1, 2, 3, 2, 1, 4, 5]
unique_elements = unique_list(input_list)
print("Unique elements:", unique_elements)
# Output: Unique elements: [1, 2, 3, 4, 5]

"""

"""
easiest way to get unique elements from a list in Python is to use the set() function.
# Example usage
input_list = [1, 2, 3, 2, 1, 4, 5]
unique_elements = list(set(input_list))
print("Unique elements:", unique_elements)
# Output: Unique elements: [1, 2, 3, 4, 5]
# This method is more efficient and concise than using a for loop.
"""