from stats import get_num_words, get_char_count, sort_character_counts 
#Import functions from stats 

def get_book_text(filepath):
    """Reads a file and returns its contents as a string."""
    with open(filepath, "r", encoding="utf-8") as f:  
        #Open the file with UTF-8 encoding
        return f.read()  #Read and return the entire file contents

def main():
    """Reads the book text, counts words, and prints the result."""
    filepath = "books/frankenstein.txt"  #Define the file path
    book_text = get_book_text(filepath)  #Read the book contents
    word_count = get_num_words(book_text)  #Count words in the text
    char_count = get_char_count(book_text) #Count character occurrences
    sorted_chars = sort_character_counts(char_count) #Sort character counts

# Print the formatted report
    print("\n============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        for char, count in char_dict.items():
            print(f"{char}: {count}")

    print("============= END ===============\n")


#Ensure the script runs only if executed directly (not imported as a module)
if __name__ == "__main__":
    main() #Run the program when executed directly 
