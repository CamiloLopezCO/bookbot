def get_book_text():
    """Reads a file and return its contents as a string."""
     # Use the 'with' block to open the file
    with open("books/frankenstein.txt") as f:
        # Read the contents of the file
        return  f.read()
def main():
    """Calls get_book_text and prints the book content."""
    book_text = get_book_text("books/frankenstein.txt")
    # Print the contents to the console
    print(book_text)

    main()
