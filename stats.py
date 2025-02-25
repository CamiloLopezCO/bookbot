def get_num_words(text):
    """Counts the number of words in the given text."""
    return len(text.split())  #Return the total number of words

def get_char_count(text):
    """Counts the number of times each character appears in the text."""
    text = text.lower() #Convert text to lowercase to avoid case difference
    char_counts = {} #Initialize an empty dictionary

    for char in text:
        if char in char_counts:
            char_counts[char] += 1 #Increment count if character exists
        else:
            char_counts[char] = 1 #Initialize count if character is new
    return char_counts #Return dictionary of character frequencies 
def sort_character_counts(char_counts):
    """Sorts the dictionary of character counts in descending order, keeping only alphabetical characters."""
    sorted_counts = sorted([{char: count} for char, count in char_counts.items() if char.isalpha()], key=lambda x: list(x.values())[0],reverse=True)
    return sorted_counts