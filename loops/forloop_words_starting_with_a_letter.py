st = 'Hi there, I am learning Python. I love Python programming.'
words = st.split()
for word in words:
    cleaned_word = word.strip('.,')  # remove common punctuation
    if cleaned_word.startswith('P') or cleaned_word.startswith('p'):
        print(cleaned_word)
# Output:
# Python
# Python
# programming
# The code iterates through each word in the string, removes common punctuation, and checks if the word starts with 'P' or 'p'. If it does, it prints the word.
