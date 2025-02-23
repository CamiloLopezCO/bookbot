from stats import get_num_words #Import word-counting function 

def get_book_text(filepath):
    """Reads a file and returns its contents as a string."""
    with open(filepath, "r", encoding="utf-8") as f:  # Open the file with UTF-8 encoding
        return f.read()  # Read and return the entire file contents

def main():
    """Reads the book text, counts words, and prints the result."""
    filepath = "books/frankenstein.txt"  # Define the file path
    book_text = get_book_text(filepath)  # Read the book contents
    word_count = get_num_words(book_text)  # Count words in the text

    # Print the total word count in the book
    print(f"{word_count} words found in the document")

# Ensure the script runs only if executed directly (not imported as a module)
if __name__ == "__main__":
    main()
